#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
题目：求100之内的素数。
分析：判断素数的方法，原始的是用除了1和自身外的其他数去除那个数，如果都不能除尽，就是，
否则就不是。一个简化的方法就是没必要用2~m-1去除，只需要用2~sqrt(m)去除就可以。
"""

from math import sqrt

def get_prime(n):
    return filter(lambda x: not [x%i for i in range(2, int(sqrt(x))+1) if x%i ==0], range(2,n+1))
print get_prime(100)

