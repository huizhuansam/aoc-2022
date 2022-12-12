import heapq
from collections import deque

import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/12/input', cookies=config)

grid = []
start = None
end = None
start_pos = []

for y, row in enumerate(r.content.strip().split(b'\n')):
    a = []
    for x, col in enumerate(row):
        if col == ord(b'S'):
            start = (x, y)
            start_pos.append((x, y))
        if col == ord(b'E'):
            end = (x, y)
        if col == ord(b'a'):
            start_pos.append((x, y))
        a.append(col)
    grid.append(a)

grid[start[1]][start[0]] = ord(b'a')
grid[end[1]][end[0]] = ord(b'z')

# Part one
q = deque([start])
visited = {start}
d = 1
e = False
deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
rows = len(grid)
cols = len(grid[0])

while q:
    for _ in range(len(q)):
        curr_x, curr_y = q.popleft()
        for dx, dy in deltas:
            next_x, next_y = curr_x + dx, curr_y + dy
            if 0 <= next_x < cols and 0 <= next_y < rows:
                if (next_x, next_y) not in visited:
                    curr_v = grid[curr_y][curr_x]
                    next_v = grid[next_y][next_x]
                    if next_v <= curr_v + 1:
                        if (next_x, next_y) == end:
                            print(d)
                            e = True
                            break
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))
    if e:
        break
    d += 1

# Part two
q = deque(start_pos)
visited = set(start_pos)
d = 1
e = False

while q:
    for _ in range(len(q)):
        curr_x, curr_y = q.popleft()
        for dx, dy in deltas:
            next_x, next_y = curr_x + dx, curr_y + dy
            if 0 <= next_x < cols and 0 <= next_y < rows:
                if (next_x, next_y) not in visited:
                    curr_v = grid[curr_y][curr_x]
                    next_v = grid[next_y][next_x]
                    if next_v <= curr_v + 1:
                        if (next_x, next_y) == end:
                            print(d)
                            e = True
                            break
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))
    if e:
        break
    d += 1
