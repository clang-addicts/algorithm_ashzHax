#!/usr/env/python3

for a in range(0, int(input())):
    arr = input().split(' ')
    loop_cnt = int(arr[0]) 
    string = arr[1]

    new = ''
    for g in list(string):
        for _ in range(0, loop_cnt):
            new = new + g
    print(new)