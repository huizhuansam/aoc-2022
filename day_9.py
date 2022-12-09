import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/9/input', cookies=config)

moves = [(chr(move[0]), int(move[2:])) for move in r.content.strip().split(b'\n')]

# Part one
head_pos = (0, 0)
tail_pos = (0, 0)
tail_visited = {(0, 0)}

deltas = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

for d, s in moves:
    for _ in range(s):
        dx, dy = deltas[d]
        head_pos = head_pos[0] + dx, head_pos[1] + dy
        del_x, del_y = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]
        if (del_x == 1 and del_y == 2) or (del_x == 2 and del_y == 1):
            tail_pos = tail_pos[0] + 1, tail_pos[1] + 1
        elif (del_x == 1 and del_y == -2) or (del_x == 2 and del_y == -1):
            tail_pos = tail_pos[0] + 1, tail_pos[1] - 1
        elif (del_x == -1 and del_y == 2) or (del_x == -2 and del_y == 1):
            tail_pos = tail_pos[0] - 1, tail_pos[1] + 1
        elif (del_x == -2 and del_y == -1) or (del_x == -1 and del_y == -2):
            tail_pos = tail_pos[0] - 1, tail_pos[1] - 1
        elif del_x == 2 and del_y == 0:
            tail_pos = tail_pos[0] + 1, tail_pos[1]
        elif del_x == -2 and del_y == 0:
            tail_pos = tail_pos[0] - 1, tail_pos[1]
        elif del_x == 0 and del_y == 2:
            tail_pos = tail_pos[0], tail_pos[1] + 1
        elif del_x == 0 and del_y == -2:
            tail_pos = tail_pos[0], tail_pos[1] - 1
        tail_visited.add(tail_pos)

print(len(tail_visited))

# Part two
knots = [(0, 0)] * 10
tail_visited = {(0, 0)}

for d, s in moves:
    for _ in range(s):
        dx, dy = deltas[d]
        head = knots[0]
        knots[0] = knots[0][0] + dx, knots[0][1] + dy
        for i in range(1, len(knots)):
            front = knots[i - 1]
            back = knots[i]
            del_x, del_y = front[0] - back[0], front[1] - back[1]
            if (del_x == 1 and del_y == 2) or (del_x == 2 and del_y == 1) or (del_x == 2 and del_y == 2):
                knots[i] = knots[i][0] + 1, knots[i][1] + 1
            elif (del_x == 1 and del_y == -2) or (del_x == 2 and del_y == -1) or (del_x == 2 and del_y == -2):
                knots[i] = knots[i][0] + 1, knots[i][1] - 1
            elif (del_x == -1 and del_y == 2) or (del_x == -2 and del_y == 1) or (del_x == -2 and del_y == 2):
                knots[i] = knots[i][0] - 1, knots[i][1] + 1
            elif (del_x == -2 and del_y == -1) or (del_x == -1 and del_y == -2) or (del_x == -2 and del_y == -2):
                knots[i] = knots[i][0] - 1, knots[i][1] - 1
            elif del_x == 2 and del_y == 0:
                knots[i] = knots[i][0] + 1, knots[i][1]
            elif del_x == -2 and del_y == 0:
                knots[i] = knots[i][0] - 1, knots[i][1]
            elif del_x == 0 and del_y == 2:
                knots[i] = knots[i][0], knots[i][1] + 1
            elif del_x == 0 and del_y == -2:
                knots[i] = knots[i][0], knots[i][1] - 1
        tail_visited.add(knots[-1])

print(len(tail_visited))
