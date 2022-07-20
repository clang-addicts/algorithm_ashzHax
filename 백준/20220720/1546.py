#!/usr/env/python3

n = int(input())
arr = input().split(' ')
_sum = 0
h = 0

for i in arr:
    if int(i) > h:
        h = int(i)

for i in arr:
    _sum += int(i)/h*100

print(str(_sum/n))