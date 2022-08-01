#!/usr/env/python3

_str = input().split(' ')
cnt = 0

for i in _str:
    if len(i) > 0:
        cnt += 1

print(str(cnt))