#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：给一个不多于5位的正整数，要求：一、求它是几位
数，二、逆序打印出各位数字。
程序分析：学会分解出每一位数。
"""

def fiveNumber(num):
	wan = num / 10000
	qian = num % 10000 / 1000
	bai = num % 1000 / 100
	shi = num % 100 / 10
	ge = num % 10

	if wan != 0:
		print "%d is 5:" % num,ge,shi,bai,qian,wan
	elif qian != 0:
		print "%d is 4:" % num,ge,shi,bai,qian
	elif bai != 0:
		print "%d is 3:" % num,ge,shi,bai
	elif shi != 0:
		print "%d is 2:" % num,ge,shi
	else:
		print "%d is 1:" % num,ge

def main():
	num = input("input a int number(don't outside 5):")
	fiveNumber(num)

if __name__ == '__main__':
	main()
