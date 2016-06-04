#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：结构体变量传递
"""

if __name__ == '__main__':
	class student:
		x = 0
		c = 0
	def f(stu):
		stu.x = 20
		stu.c = 'c'
	a = student() # 实例化student类的一个实例
	a.x = 3 # 这两句实际上是没什么作用的
	a.c = 'a'
	f(a)
	print a.x,a.c