#!/usr/env/python3

a,b = input().split(' ')

if int(a)>int(b):
    print('>')
elif int(a)<int(b):
    print('<')
else:
    print('==')