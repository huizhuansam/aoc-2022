import functools

import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/3/input', cookies=config)

rucksacks = r.content.strip().split(b'\n')

# Part one
print(sum([
    c - 96 if 97 <= c <= 122 else c - 38 for c in [
        set(a).intersection(set(b)).pop() for a, b in [
            (rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in rucksacks]]]))

# Part two
print(sum([
    c - 96 if 97 <= c <= 122 else c - 38 for c in [
        functools.reduce(lambda a, b: a.intersection(b), rucksack).pop() for rucksack in [
            [set(rucksack) for rucksack in rucksacks[i: i + 3]] for i in range(0, len(rucksacks), 3)]]]))
