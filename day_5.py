import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/5/input', cookies=config)

puzzle = r.content.strip().split(b'\n\n')
initial = [[row[i:i + 4].strip() for i in range(0, len(row), 4)] for row in puzzle[0].split(b'\n')][:-1]
moves = [(int(token[1]), int(token[3]), int(token[5])) for token in [move.split(b' ') for move in puzzle[1].split(b'\n')]]

# Part one
rotated = [[elem.strip(b'[]') for elem in col if elem != b''] for col in list(map(list, zip(*initial[::-1])))]

for qty, src, dst in moves:
    for _ in range(qty):
        rotated[dst - 1].append(rotated[src - 1].pop())

print(b''.join([col[-1] for col in rotated]).decode())

# Part two
rotated = [[elem.strip(b'[]') for elem in col if elem != b''] for col in list(map(list, zip(*initial[::-1])))]

for qty, src, dst in moves:
    rotated[dst - 1] = rotated[dst - 1] + rotated[src - 1][-qty:]
    rotated[src - 1] = rotated[src - 1][:-qty]

print(b''.join([col[-1] for col in rotated]).decode())
