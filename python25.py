#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
"""

#最简单的方法就是用lambda配合reduce函数来做
def factorialSum(n):
	sum = 0
	for i in range(1,n+1):
		t = reduce(lambda x,y:x*y,range(1,i+1))#计算阶乘
		sum += t
	print sum

def main():
	factorialSum(20)

if __name__ == '__main__':
	main()