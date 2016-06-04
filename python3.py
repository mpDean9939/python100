#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
题目：一个整数，它加上100和加上268后都是一个完全平方数，
请问该数是多少？
程序分析：在10000以内判断，将该数加上100后再开方，加上268后
再开方，如果开方后的结果满足如下条件，即是结果。
"""

import math #要用到开方，所以需要导入math包
for i in range(10000):#在10000内判断
    #考虑到开方后有可能是小数，所以需要转化成整形
    sqrtone = int(math.sqrt(i + 100))
    sqrttwo = int(math.sqrt(i + 268))
    if(sqrtone * sqrtone == i + 100) and (sqrttwo * sqrttwo == i + 268):
    	print i
"""
结果：
21
261
1581
"""