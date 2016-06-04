#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，
然后再加上5天即本年的第几天，
特殊情况，闰年的2月是29天，如果年份是闰年，并且闰年的
月份在3月以后，则需要多加1天。
每四年一次闰年。
1,3,5,7,8,10,12月是31天，2月是28天，其他的是30天。
"""

year = int (raw_input('year:\n'))
month = int (raw_input('month:\n'))
day = int (raw_input('day:\n'))

months = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0<month<=12:
	sum = months[month - 1]
else:
	print 'data error'
sum += day

leap = 0
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
	leap = 1
if (leap == 1) and (month >2):
	sum += 1
	
print 'It is the %dth day.'% sum
