#!/usr/env/python3

while True:
    try:
        a,b = input().split(' ')
        cur = int(a)+int(b)
        print(str(cur))
    except:
        break