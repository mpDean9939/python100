#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，
个位与万位相同，十位与千位相同。
"""

def main():
	number = int(raw_input('input an 5 bit int number:\n'))
	num = str(number)
	flag = 1
	for i in range(len(num)/2):
		if num[i] != num[-i-1]:
			flag = 0
			break
	if flag:
		print u"%d是一个回文数！".encode('gbk') % number
	else:
		print u"%d不是一个回文数！".encode('gbk') % number

if __name__ == '__main__':
	main()