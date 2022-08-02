#!/usr/env/python3

def rev(n):
    arr = list(str(n))
    ptr = len(arr)
    narr = [0] * 3
    _str = ''
    for i in arr:
        narr[ptr-1] = i
        ptr -= 1
    for i in narr:
        _str += i
    return int(_str)

a,b = map(int, input().split(' '))

a = rev(a)
b = rev(b)

if a > b:
    print(a)
else:
    print(b)