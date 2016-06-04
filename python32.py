#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：按相反的顺序输出列表的值。
"""

def outabverse():
	lista = ['one','two','three']
	for i in lista[::-1]:
		print i,
	print

def main():
	outabverse()

if __name__ == '__main__':
	main()