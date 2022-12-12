import copy
import functools

import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/11/input', cookies=config)

op_dict = {
    b'+': lambda x: lambda y: x + y,
    b'*': lambda x: lambda y: x * y,
}

# Part one
monkey_items_1 = []
operations = []
divisor_tests = []
true_monkeys = []
false_monkeys = []
monkey_processed = []

for monkey_string in r.content.strip().split(b'\n\n'):
    token = [m.strip().split(b':')[1].strip() for m in monkey_string.split(b'\n')[1:]]
    monkey_items_1.append([int(t) for t in token[0].split(b', ')])
    l_operand, operator, r_operand = token[1].split(b' = ')[1].split(b' ')
    if l_operand == r_operand and l_operand == b'old':
        operations.append(lambda x: x * x)
    else:
        operations.append(op_dict[operator](int(r_operand)))
    divisor_tests.append(int(token[2].split(b' by ')[1]))
    true_monkeys.append(int(token[3].split(b' monkey ')[1]))
    false_monkeys.append(int(token[4].split(b' monkey ')[1]))
    monkey_processed.append(0)

monkey_items_2 = copy.deepcopy(monkey_items_1)
monkey_processed_2 = copy.deepcopy(monkey_processed)

for _ in range(20):
    for i, monkey_item in enumerate(monkey_items_1):
        for item in monkey_item:
            worry = operations[i](item) // 3
            if worry % divisor_tests[i] == 0:
                monkey_items_1[true_monkeys[i]].append(worry)
            else:
                monkey_items_1[false_monkeys[i]].append(worry)
        monkey_processed[i] += len(monkey_item)
        monkey_item.clear()

monkey_processed.sort()
print(monkey_processed[-1] * monkey_processed[-2])

# Part two
lcm = functools.reduce(lambda x, y: x * y, divisor_tests)

for _ in range(10000):
    for i, monkey_item in enumerate(monkey_items_2):
        for item in monkey_item:
            worry = operations[i](item) % lcm
            if worry % divisor_tests[i] == 0:
                monkey_items_2[true_monkeys[i]].append(worry)
            else:
                monkey_items_2[false_monkeys[i]].append(worry)
        monkey_processed_2[i] += len(monkey_item)
        monkey_item.clear()

monkey_processed_2.sort()
print(monkey_processed_2[-1] * monkey_processed_2[-2])
