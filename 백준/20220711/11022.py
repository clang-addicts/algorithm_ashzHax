#!/usr/env/python3

n = int(input())
for i in range(1, n+1):
    a,b=input().split(' ')
    print('Case #'+str(i)+': '+a+' + '+b+' = '+str(int(a)+int(b)))