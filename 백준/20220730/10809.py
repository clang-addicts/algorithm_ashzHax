#!/usr/env/python3

word = input()
alpha = [-1]*26
loc = 0

for i in word:
    nloc = ord(i)-97
    if alpha[nloc] != -1:
        loc +=  1
        continue
    alpha[nloc] = loc
    loc +=  1


for i in alpha:
    print(i, end=' ')