#!/usr/env/python3

while True:
    a,b = input().split(' ')
    if int(a) == 0 and int(b) == 0:
        break
    print(str(int(a)+int(b)))