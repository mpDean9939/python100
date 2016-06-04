#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：利用递归方法求5!。
程序分析：递归公式：f(n)!=f(n)*f(n-1)!
"""

def fact(j):
    sum = 0
    if j == 0 or j == 1:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum

def main():
	for i in range(5):
	    print '%d! = %d' % (i,fact(i))

if __name__ == '__main__':
	main()
