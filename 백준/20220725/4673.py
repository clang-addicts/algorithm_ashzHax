#!/usr/env/python3

def _self(n):
    _sum = 0
    tmp = n
    while tmp > 0:
        _sum += tmp % 10
        tmp = int(tmp/10)
    return n + _sum

arr = []
for i in range(1, 10000+1):
    arr.append(_self(i))

for i in range(1, 10000+1):
    if not i in arr:
        print(i)