#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""

"""
方法一：循环方法
"""
def fib(n):
	a,b = 0,1
	for i in range(n-1):
		a,b = b,a+b
	return a

print fib(2)

"""
方法二：递归
"""
def fib1(n):
	if n==1 or n==2:
		return 1#1,1,2,3,5,8.....
	return fib1(n-1)+fib1(n-2)

print fib1(10)

"""
方法三：输出整个数列
a=[1,2,3]
a[-1]=3
a[-2]=2
"""
def fib2(n):
	if n == 1:
		return [1]
	if n == 2:
		return [1,1]
	fibs = [1,1]
	for i in range(2,n):
		fibs.append(fibs[-1]+fibs[-2])#这里采用-1和-2就是保证一直用列表里最新的两个元素去计算
	return fibs

print fib2(10)