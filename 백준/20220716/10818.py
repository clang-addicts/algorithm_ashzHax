#!/usr/env/python3

min = 1000001
max = -1000001

n = int(input())
arr = input().split(' ')

for i in arr:
    t = int(i)
    if t < min:
        min = t 
    if t > max:
        max = t

print(str(min)+' '+str(max))