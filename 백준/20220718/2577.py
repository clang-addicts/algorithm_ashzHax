#!/usr/env/python3

arr = [0,0,0,0,0,0,0,0,0,0]

a = int(input())
b = int(input())
c = int(input())
res = a*b*c

while res > 0:
    #print('res='+str(res)+' res%10='+str(res%10))
    arr[res%10] += 1
    res = int(res/10)

for i in arr:
    print(str(i))