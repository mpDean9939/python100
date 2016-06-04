#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：暂停一秒输出。
程序分析：需要time模块。
"""

import time

myD = {1:'A',2:'B'}
for key,value in dict.items(myD):
	print key,':',value
	time.sleep(1)#sleep表示程序等一段时间，什么都不干，不推荐使用
#实际效果就是，在输出1:A后，会等一秒在输出2:B