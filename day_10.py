import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/10/input', cookies=config)

instructions = r.content.strip().split(b'\n')

# Part one
X = 1
cycle = 1
signal_sum = 0
target_cycles = {20, 60, 100, 140, 180, 220}

for instruction in instructions:
    if instruction == b'noop':
        if cycle in target_cycles:
            signal_sum += cycle * X
        cycle += 1
    else:
        val = int(instruction.split(b' ')[1])
        for _ in range(2):
            if cycle in target_cycles:
                signal_sum += cycle * X
            cycle += 1
        X += val

print(signal_sum)

# Part two
line = ''
pos = 0
X = 1
end_of_line = 39

for instruction in instructions:
    if instruction == b'noop':
        if pos in {X - 1, X, X + 1}:
            line += '#'
        else:
            line += '.'
        if pos == end_of_line:
            print(line)
            line = ''
            pos = 0
        else:
            pos += 1
    else:
        val = int(instruction.split(b' ')[1])
        for _ in range(2):
            if pos in {X - 1, X, X + 1}:
                line += '#'
            else:
                line += '.'
            if pos == end_of_line:
                print(line)
                line = ''
                pos = 0
            else:
                pos += 1
        X += val

print(line)
