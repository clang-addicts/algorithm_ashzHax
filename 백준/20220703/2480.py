#!/usr/env/python3

sa,sb,sc = input().split(' ')
a = int(sa)
b = int(sb)
c = int(sc)
reward = 0

if a==b and b==c:
    reward = 10000+(a*1000)
elif a==b:
    reward = 1000+(a*100) 
elif a==c:
    reward = 1000+(a*100) 
elif c==b:
    reward = 1000+(c*100) 
else:
    if a>b and a>c:
        reward = a*100
    elif b>a and b>c:
        reward = b*100
    else:
        reward = c*100

print(reward)