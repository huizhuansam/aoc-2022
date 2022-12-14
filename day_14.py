import copy

import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/14/input', cookies=config)

puzzle = [[tuple([int(i) for i in p.split(b',')]) for p in l.split(b' -> ')] for l in r.content.strip().split(b'\n')]
obstacles = set()

for line in puzzle:
    for i in range(len(line) - 1):
        a_x, a_y = line[i]
        b_x, b_y = line[i + 1]
        if a_x == b_x:
            for y in range(a_y if a_y < b_y else b_y, (b_y if a_y < b_y else a_y) + 1):
                obstacles.add((a_x, y))
        if a_y == b_y:
            for x in range(a_x if a_x < b_x else b_x, (b_x if a_x < b_x else a_x) + 1):
                obstacles.add((x, b_y))

# Part one
res = 0
out = False
p1_obs = copy.deepcopy(obstacles)
lowest_point = max([o[1] for o in p1_obs])


def is_blocked(col, row):
    return (col, row + 1) in p1_obs and (col + 1, row + 1) in p1_obs and (col - 1, row + 1) in p1_obs


while True:
    x, y = 500, 0
    while not is_blocked(x, y):
        if (x, y + 1) not in p1_obs:
            y = y + 1
        elif (x - 1, y + 1) not in p1_obs:
            x = x - 1
            y = y + 1
        elif (x + 1, y + 1) not in p1_obs:
            x = x + 1
            y = y + 1
        if y > lowest_point:
            out = True
            print(res)
            break
    if out:
        break
    p1_obs.add((x, y))
    res += 1

# Part two
res = 0
p2_obs = copy.deepcopy(obstacles)
floor = lowest_point + 2


def blocked(col, row):
    return ((col, row + 1) in p2_obs and (col - 1, row + 1) in p2_obs and (col + 1, row + 1) in p2_obs) or row == (
                floor - 1)


while True:
    x, y = 500, 0
    while not blocked(x, y):
        if (x, y + 1) not in p2_obs:
            y = y + 1
        elif (x - 1, y + 1) not in p2_obs:
            x = x - 1
            y = y + 1
        elif (x + 1, y + 1) not in p2_obs:
            x = x + 1
            y = y + 1
    if (x, y) == (500, 0):
        print(res + 1)
        break
    p2_obs.add((x, y))
    res += 1
