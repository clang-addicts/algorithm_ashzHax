#!/usr/env/python3

stupid_year = int(input())

if (stupid_year % 400 == 0) or (stupid_year % 4 == 0 and stupid_year % 100 != 0):
    print('1')
else:
    print('0')