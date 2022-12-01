import requests
import heapq
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/1/input', cookies=config)

calorie_sum = [sum([int(calorie) for calorie in calories.split(b'\n')]) for calories in r.content.strip().split(b'\n\n')]

# Part one
print(max(calorie_sum))

# Part two
print(sum(heapq.nlargest(3, calorie_sum)))
