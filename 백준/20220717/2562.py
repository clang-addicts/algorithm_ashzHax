#!/usr/env/python3

arr = []
h = 0
idx = 0

for i in range(0,9):
    t = int(input())
    if t > h:
        h = t
        idx = i

print(h)
print(idx+1)