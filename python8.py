#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""

for r in range(1,10):
	for l in range(1,r+1):#用r+1做控制，用来消除重复的部分
		result = r*l
		print '%d * %d = % d' % (r,l,result),#加了逗号，不让print自动换行
	print '\n'