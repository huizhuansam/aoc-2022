import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/6/input', cookies=config)

puzzle = r.content.strip()

# Part one
for rp in range(4, len(puzzle)):
    lp = rp - 4
    marker = puzzle[lp: rp]
    if len(set(marker)) == 4:
        print(rp)
        break

# Part two
for rp in range(14, len(puzzle)):
    lp = rp - 14
    marker = puzzle[lp: rp]
    if len(set(marker)) == 14:
        print(rp)
        break
