#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt
(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""

totalNum = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
	k = int(sqrt(m+1))
	for i in range(2,k+1):#左开右闭，所以k+1
		if m % i == 0:
			leap = 0#不是素数的情况下leap=0，
			break
	if leap == 1:
		print '%d' % m
		totalNum += 1
		if totalNum % 5 == 0:
			print ''#5个一组输出，便于统计
	leap = 1#每次循环完了都要把leap恢复成1
print 'The total is %d' % totalNum


"""
什么的方法感觉很臃肿，还有以下方法
"""

#用python的数学函数

import math 

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
		return True

#单行程序扫描素数    
   
from math import sqrt    
N = 201   
a = [ p for p in range(101, N) if 0 not in [ p % d for d in range(2, int(sqrt(p))+1)] ]
print a,'\n',u'素数总数有：%d个'.encode('gbk') % len(a)