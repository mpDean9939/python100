#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：809*??=800*??+9*??+1 其中??代表的两位数,
8*??的结果为两位数，9*??的结果为3位数。求??代表
的两位数，及809*??后的结果。
"""

originNum = 809
for i in range(10,100):
	right = 800 * i + 9 * i + 1
	left = originNum * i
	if left == right:
		if 8 * i > 9 and 8 * i < 100 and \
		9 * i > 99 and 9 * i < 1000:
			print i,809 * i
		# break


