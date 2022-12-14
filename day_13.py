import ast
import functools
import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/13/input', cookies=config)

signals = [[ast.literal_eval(s.decode()) for s in p.split(b'\n')] for p in r.content.strip().split(b'\n\n')]


def is_in_order(left, right):
    if type(left) is list and type(right) is list:
        len_l = len(left)
        len_r = len(right)
        for i in range(len_l):
            if i >= len_r:
                return -1
            l = left[i]
            r = right[i]
            order = is_in_order(l, r)
            if order != 0:
                return order
        if len_l == len_r:
            return 0
        return 1
    if type(left) is int and type(right) is int:
        if left > right:
            return -1
        if left < right:
            return 1
        return 0
    if type(left) is int:
        return is_in_order([left], right)
    return is_in_order(left, [right])


# Part one
print(sum([(i + 1) if is_in_order(signal[0], signal[1]) == 1 else 0 for i, signal in enumerate(signals)]))

# Part two
all_signals = [signal[0] for signal in signals] + [signal[1] for signal in signals]
all_signals.append([[2]])
all_signals.append([[6]])
sorted_signals = sorted(all_signals, key=functools.cmp_to_key(is_in_order), reverse=True)
print((sorted_signals.index([[2]]) + 1) * (sorted_signals.index([[6]]) + 1))
