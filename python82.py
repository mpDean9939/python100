#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
八进制转换为十进制
"""

if __name__ == '__main__':
	n = 0
	p = []
	for j in range(2):
		p.append(input('input a octal number:\n'))
	# p = input('input a octal number:\n')
	for i in range(2):
		n = n + p[i] * 8 ** i
	# m = int(p,8) # 第二种方法
	print n
