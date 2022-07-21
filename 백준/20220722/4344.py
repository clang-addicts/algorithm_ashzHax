#!/usr/env/python3

n = int(input())

for _ in range(0, n):
    arr = input().split()
    _cnt = int(arr.pop(0))
    _sum =  0
    for jdx in arr:
        _sum += int(jdx)

    avg = _sum/_cnt
    _sum = 0
    for jdx in arr:
        if int(jdx) > avg:
            _sum += 1
    
    print('{:.3f}%'.format(_sum/_cnt*100))