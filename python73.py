#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：反向输出一个链表。
"""

if __name__ == '__main__':
	ptr = []
	for i in range(5):
		num = int(raw_input('input a number:\n'))
		ptr.append(num)

	print ptr
	ptr.reverse()
	print ptr
