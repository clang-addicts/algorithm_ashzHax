#!/usr/env/python3

sh,sm = input().split(' ')
t = int(input())
h = int(sh)
m = int(sm)

h += int(t/60)
m += int(t%60)

if m>=60:
    h += 1
    m %= 60

h %= 24
print(str(h)+' '+str(m))