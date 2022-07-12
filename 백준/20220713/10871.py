#!/usr/env/python3

ta,tb = input().split(' ')
cnt = int(ta)
_min = int(tb)
arr = input().split(' ')

for i in arr:
    if int(i) < _min:
        print(i, end=' ')