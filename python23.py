#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import stdout

"""
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
程序分析：先把图形分成两部分来看待，前四行
一个规律，后三行一个规律，利用双重for循环，
第一层控制行，第二层控制列

每一部分分为两个工作，打印空格和打印*号
"""

def printDiamondUp(rowUp):
	for rowNum in range(rowUp):
		for spaceNum in range(3 - rowNum):
			stdout.write(' ')
		for starNum in range(2 * rowNum + 1):
			stdout.write('*')
		print #print后面自带回车

def printDiamondDown(rowDown):
	for rowNum in range(rowDown):
		for spaceNum in range(rowNum + 1):
			stdout.write(' ')
		for starNum in range(5 - 2 * rowNum):
			stdout.write('*')
		print

def main():
	printDiamondUp(4)
	printDiamondDown(3)

if __name__ == '__main__':
	main()