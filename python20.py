#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度
的一半；再落下，求它在第10次落地时，共经过多少米？第10
次反弹多高？
程序分析：
"""

def getL(startHigh,num):
	sum = 100.0
	Hn = sum / 2
	for i in range(2,num):
		sum = sum + 2 * Hn#这里之所以要*2是因为来回两次，
		Hn = Hn / 2
	return sum

def main():
	print getL(100,11)

if __name__=='__main__':
	main()