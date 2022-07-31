#!/usr/env/python3

a = input()
alpha = [0]*26

for i in list(a.upper()):
    idx = ord(i)-ord('A')
    #print('idx='+str(idx))
    alpha[idx] += 1

h = 0
same = 0
ch = ''
cnt = 0
for i in alpha:
    if h < i:
        h = i
        ch = chr(cnt+ord('A'))
        same = 0
    elif h == i:
        same = 1
    cnt += 1

#print('h='+str(h)+' same='+str(same))
if same == 1:
    print('?')
else:
    print(ch)