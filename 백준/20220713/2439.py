#!/usr/env/python3

n = int(input())

for i in range(0,n):
    for k in range(i, n-1):
        print(' ', end='')
    for j in range(0,i+1):
        print('*', end='')
    print('')