#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
题目：对10个数进行排序。
程序分析：利用选择法，即从后9个比较过程中，
选择一个最小的与第一个元素交换，下次类推，即用第
二个元素与后8个进行比较，并进行交换。
"""

def getNum(num):
	print 'Please input %d num:\n' % num
	l = []
	for i in range(num):
		l.append(int(raw_input('input a number:\n')))
	print
	print 'before sorted:'
	for i in range(len(l)):
		print l[i],
	sortNum(l)

#sort
def sortNum(l):
	for i in range(len(l)-1):
		minNum = i
		for j in range(i+1,len(l)):
			if l[minNum] > l[j]:
				minNum = j
		l[i],l[minNum]= l[minNum],l[i]#这样做，省略了中间变量temp的运用
	printSort(l)

def printSort(l):
	print 'after sorted:'
	for i in range(len(l)):
		print l[i]

def main():
	getNum(5)


if __name__ == '__main__':
	main()
	

