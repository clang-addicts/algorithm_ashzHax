#!/usr/env/python3

arr = []
diff_arr = []

for _ in range(0,10):
    arr.append(int(input())%42)

for i in arr:
    diff_flag = True
    for j in diff_arr:
        if i == j:
            diff_flag = False 
    if diff_flag:
        diff_arr.append(i)

print(len(diff_arr))