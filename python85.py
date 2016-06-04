#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：判断一个素数能被几个9整除。
分析：素数能被9整除？？？？这个程序没意义。。。

"""

if __name__ == '__main__':
	zi = int(raw_input('input a number:\n'))
	n1 = 1
	c9 = 1
	m9 = 9
	sum = 9
	while n1 != 0:
		if sum % zi == 0:
			n1 = 0
		else:
			m9 *= 10
			sum += m9
			c9 += 1
	print '%d can be divide by %d 9' % (sum,c9)