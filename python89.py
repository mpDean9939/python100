#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：某个公司采用公用电话传递数据，数据是
四位的整数，在传递过程中是加密的，加密规则
如下：每位数字都加上5,然后用和除以10的余数
代替该数字，再将第一位和第四位交换，第二位
和第三位交换。
"""

from sys import stdout
if __name__ == '__main__':
	originData = int(raw_input('input a 4 bit number:\n'))
	divData = [] # 用来存放分解后的这个4位数的各个位的数
	divData.append(originData % 10)
	divData.append(originData % 100 /10)
	divData.append(originData % 1000 /100)
	divData.append(originData / 1000)

	# 加密
	for i in range(4):
		divData[i] += 5
		divData[i] %= 10
	for j in range(2):
		divData[j],divData[3 - j] = divData[3 - j],divData[j]

	#输出
	for k in range(3,-1,-1):
		stdout.write(str(divData[k]))
