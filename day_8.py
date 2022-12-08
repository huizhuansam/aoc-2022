import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = r = requests.get('https://adventofcode.com/2022/day/8/input', cookies=config)

grid = [[int(chr(col)) for col in row] for row in r.read().strip().split(b'\n')]
rows = len(grid)
cols = len(grid[0])

# Part one
top_view = [(col, 0, grid[0][col]) for col in range(cols)]
left_view = [(0, row, grid[row][0]) for row in range(rows)]
right_view = [(cols - 1, row, grid[row][cols - 1]) for row in range(rows)]
bottom_view = [(col, rows - 1, grid[rows - 1][col]) for col in range(cols)]
can_see = {view for view in ([(col, 0) for col in range(cols)] +
                             [(0, row) for row in range(rows)] +
                             [(cols - 1, row) for row in range(rows)] +
                             [(col, rows - 1) for col in range(cols)])}

while top_view:
    curr_x, curr_y, curr_max = top_view.pop()
    next_x, next_y = curr_x, curr_y + 1
    if 0 <= next_x < cols and 0 <= next_y < rows:
        next_h = grid[next_y][next_x]
        if next_h > curr_max:
            can_see.add((next_x, next_y))
        top_view.append((next_x, next_y, max(next_h, curr_max)))

while left_view:
    curr_x, curr_y, curr_max = left_view.pop()
    next_x, next_y = curr_x + 1, curr_y
    if 0 <= next_x < cols and 0 <= next_y < rows:
        next_h = grid[next_y][next_x]
        if next_h > curr_max:
            can_see.add((next_x, next_y))
        left_view.append((next_x, next_y, max(next_h, curr_max)))

while right_view:
    curr_x, curr_y, curr_max = right_view.pop()
    next_x, next_y = curr_x - 1, curr_y
    if 0 <= next_x < cols and 0 <= next_y < rows:
        next_h = grid[next_y][next_x]
        if next_h > curr_max:
            can_see.add((next_x, next_y))
        right_view.append((next_x, next_y, max(next_h, curr_max)))

while bottom_view:
    curr_x, curr_y, curr_max = bottom_view.pop()
    next_x, next_y = curr_x, curr_y - 1
    if 0 <= next_x < cols and 0 <= next_y < rows:
        next_h = grid[next_y][next_x]
        if next_h > curr_max:
            can_see.add((next_x, next_y))
        bottom_view.append((next_x, next_y, max(next_h, curr_max)))

print(len(can_see))


# Part two
res = 0

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        curr_h = grid[row][col]
        l = 0
        r = 0
        u = 0
        d = 0

        for x in range(col - 1, -1, -1):
            l_h = grid[row][x]
            l += 1
            if l_h >= curr_h:
                break

        for x in range(col + 1, cols):
            r_h = grid[row][x]
            r += 1
            if r_h >= curr_h:
                break

        for y in range(row - 1, -1, -1):
            u_h = grid[y][col]
            u += 1
            if u_h >= curr_h:
                break

        for y in range(row + 1, rows):
            d_h = grid[y][col]
            d += 1
            if d_h >= curr_h:
                break

        res = max(res, u * d * l * r)

print(res)