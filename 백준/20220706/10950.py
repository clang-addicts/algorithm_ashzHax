#!/usr/env/python3

t = int(input())
arr = []

for i in range(t):
    a,b = input().split(' ')
    arr.append(int(a)+int(b))

for i in range(t):
    print(str(arr[i]))