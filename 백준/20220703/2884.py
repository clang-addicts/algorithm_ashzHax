#!/usr/env/python3

stra,strb=input().split(' ')
a = int(stra)
b = int(strb)
r = 45

b = b - r
if b<0:
    r = (-1) * b
    a -= 1
    b = 60 - r
if a<0:
    a=23
print(str(a)+' '+str(b))