#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：利用递归函数调用方式，将所输入的5个字符，
以相反顺序打印出来。
"""

def output(s,l):
	if l != 0:
		print (s[l-1]),
		print '-',
	else:
		return
	output(s,l-1)

def main():
	s = raw_input('Input a string:')
	l = len(s)
	output(s,l)

if __name__ == '__main__':
	main()