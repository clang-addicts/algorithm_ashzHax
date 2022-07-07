#!/usr/enb/python3
import sys

a = int(input())

for i in range(a):
    a,b=sys.stdin.readline().rstrip().split(' ')
    print(int(a)+int(b))