#!/usr/env/python3

ori = int(input())
n = ori
cnt = 0

while True:
    if n < 10:
        ten = 0
    else:
        ten = int(n / 10)
    one = n % 10
    
    n = (one * 10) + ((ten+one)%10)
    cnt += 1
    if n == ori:
        break
print(cnt)