#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：字符串日期转换为易读的日期格式。
dateutil需要额外安装
"""

from dateutil import parser

dt = parser.parse('June 4 2016 11:45AM')
print dt