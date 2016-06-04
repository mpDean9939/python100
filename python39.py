#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：有一个已经排好序的数组。现输入一个数，要求按原
来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑
插入中间的数的情况，插入后此元素之后的数，依次后移
一个位置。
"""

def main():
	a = [1,2,5,6,12,34,56,79]
	listLen = len(a)
	print 'Original list is:'
	for i in range(len(a)):
		print a[i],
	print
	newNumber = int(raw_input('Insert a new number:\n'))
	end = a[listLen-1]
	if newNumber >= end:
		a.append(newNumber)
		listLen = len(a)
	else:
		for i in range(listLen):
			if a[i] > newNumber:
				b = a[i:]
				d = a[0:i]
				d.append(newNumber)
				break # 这里加break是因为只插入一个数，所以只进行一次插入和一个循环的移动就可以了
	c = d + b
	print 'After insert a new number:'			
	for k in range(len(c)):
		print c[k],

if __name__ == '__main__':
	main()
