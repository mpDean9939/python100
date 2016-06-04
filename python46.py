#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
"""

def squareNum(x):
    return x * x

def main():
    print u'如果平方运算后小于 50，程序将停止运行。'.encode('gbk')
    again = 1
    while again:
    	num = int(raw_input('Please input number:'))
    	print u'运算结果为：%d'.encode('gbk') % (squareNum(num))
    	if squareNum(num) >= 50:
    		again = 1
    	else:
    		again = 0

if __name__ == '__main__':
	main()