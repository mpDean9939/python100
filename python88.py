#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：读取7个数（1—50）的整数值，每读取一个值，
程序打印出该值个数的＊。
分析：没要求具体打印格式，所以很容易实现
"""

if __name__ == '__main__':
	n = 1
	#这里更好的实现方式是把输入写入一个单独的函数里
	while n <= 7:
		a = int(raw_input('input a number between 1 to 50:\n'))
		while a < 1 or a > 50:
			a = int(raw_input('input a number between 1 to 50:\n'))
		print a * '*'
		n += 1