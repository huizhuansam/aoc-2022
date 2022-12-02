import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/2/input', cookies=config)

games = [game_round.split(b' ') for game_round in r.content.strip().split(b'\n')]

# Part one
score = {
    b'X': 1,
    b'Y': 2,
    b'Z': 3,
}

beats = {
    b'X': b'C',
    b'Y': b'A',
    b'Z': b'B',
    b'A': b'Z',
    b'B': b'X',
    b'C': b'Y',
}


def get_result(my_shape, opponent_shape):
    if beats[my_shape] == opponent_shape:
        return 6
    if beats[opponent_shape] == my_shape:
        return 0
    return 3


def get_score(play):
    opponent_shape = play[0]
    my_shape = play[1]
    result = get_result(my_shape, opponent_shape)
    shape_score = score[my_shape]
    return result + shape_score


print(sum(map(get_score, games)))


# Part two
result_score = {
    b'X': 0,
    b'Y': 3,
    b'Z': 6,
}

to_win = {
    b'A': 2,
    b'B': 3,
    b'C': 1,
}

to_lose = {
    b'A': 3,
    b'B': 1,
    b'C': 2,
}

to_draw = {
    b'A': 1,
    b'B': 2,
    b'C': 3,
}


def my_move(opponent_shape, round_result):
    if round_result == b'X':
        return to_lose[opponent_shape]
    if round_result == b'Y':
        return to_draw[opponent_shape]
    return to_win[opponent_shape]


def calculate(play):
    opponent_shape = play[0]
    round_result = play[1]
    return result_score[round_result] + my_move(opponent_shape, round_result)


print(sum(map(calculate, games)))
