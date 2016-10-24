#encoding:utf-8

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

import datetime
import time

date = input('please input a date（like: 20161019）: ')

str_date = str(date)
year = int(str_date[0:4])
month = int(str_date[4:6])
day = int(str_date[-2:])

days_per_month = {'1': 0, '2': 31, '3': 59, '4': 90, '5': 120, '6': 151, '7': 181, '8': 212, '9': 243, '10': 273, '11': 304, '12': 334}

day_of_year = days_per_month[str(month)] + day

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month >= 3:
    day_of_year += 1 

print day_of_year	





