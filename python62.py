#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：查找字符串。
函数原型：find(str, pos_start, pos_end)

解释：

str:被查找“字串”
pos_start:查找的首字母位置（从0开始计数。默认：0）
pos_end: 查找的末尾位置（默认-1）
返回值：如果查到：返回查找的第一个出现的位置。否则，返回-1。　
"""

sStr1 = 'abcdefg'
sStr2 = 'cde'
sStr3 = 'qq'
print sStr1.find(sStr2)
print sStr1.find(sStr3)