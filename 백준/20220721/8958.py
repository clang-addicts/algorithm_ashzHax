#!/usr/env/python3

carr = []
n = int(input())

for _ in range(0, n):
    carr.append(input())

for idx in carr:
    _list = list(idx)
    streak = 0
    point = 0
    for i in _list:
        if i == 'O':
            point = point + 1 + streak
            streak += 1
        if i == 'X':
            streak = 0
    print(point)