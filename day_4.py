import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/4/input', cookies=config)
a = [assignment.split(b',') for assignment in r.content.strip().split(b'\n')]


def splitter(assignment):
    a1 = assignment[0].split(b'-')
    a2 = assignment[1].split(b'-')
    a1min = int(a1[0])
    a1max = int(a1[1])
    a2min = int(a2[0])
    a2max = int(a2[1])
    return a1min, a1max, a2min, a2max


# Part one
def contain(assignment):
    a1min, a1max, a2min, a2max = splitter(assignment)
    if (a1min <= a2min and a1max >= a2max) or (a2min <= a1min and a2max >= a1max):
        return 1
    return 0


print(sum(map(contain, a)))


# Part two
def overlap(assignment):
    a1min, a1max, a2min, a2max = splitter(assignment)
    if not (a1min > a2max or a2min > a1max):
        return 1
    return 0


print(sum(map(overlap, a)))
