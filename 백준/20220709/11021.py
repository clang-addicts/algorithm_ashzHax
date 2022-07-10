#!/usr/env/python3

a = int(input())

for i in range(1,a+1):
    b,c=input().split(' ')
    print('Case #'+str(i)+': '+str(int(b)+int(c)))
