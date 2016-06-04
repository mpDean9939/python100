#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：统计 1 到 100 之和。
"""

def twoBiteSum():
    tmp = 0
    for i in range(1,101):
        tmp += i
    print 'The sum is %d' % tmp

def main():
    twoBiteSum()

if __name__ == '__main__':
	main()