#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。或者用另一个空的数组重新放一遍
"""

def reverseList(nList):
	N = len(nList)
	print nList
	for i in range(len(nList)/2):
		nList[i],nList[N-i-1] = nList[N-i-1],nList[i]
	print nList

def newList(nList):
	print nList[::-1],

def main():
	aList = [1,2,3,4,5]
	bList = aList[:]
	cList = aList[:]
	reverseList(bList)
	newList(cList)

if __name__ == '__main__':
	main()