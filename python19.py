#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import stdout

"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
程序分析：请参照程序Python 练习实例14。
"""

for j in range(2,1001):
	yinzi = []
	yinziNum = -1
	s = j
	for i in range(1,j):
		if j % i == 0:
			yinzi.append(i)
			yinziNum += 1
			s -= i#如果最终能够达到s==0，说明就是完数。转入下面的程序

	if s == 0:
		print j
		for i in range(yinziNum):
			stdout.write(str(yinzi[i]))
			stdout.write(' ')
		print yinzi[yinziNum]