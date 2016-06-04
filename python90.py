#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：列表使用实例。
"""

# 新建list
testList = [10086,u'中国移动',[1,2,3,4]]
print len(testList)
print testList[1:]
testList.append('I\'m new here!')
print len(testList)
print testList[-1]
print testList.pop(1)
print len(testList)
print testList

matrix = [[1,2,3],
[4,5,6],
[7,8,9]]
print matrix
print matrix[1]  
col2 = [row[1] for row in matrix]#get a  column from a matrix  
print col2  
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item  
print col2even  