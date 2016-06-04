#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：暂停一秒输出。
"""
import time

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#暂停一秒
time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

"""
Python time strftime() 函数接收以时间元组，并返回以可读字
符串表示的当地时间，格式由参数format决定。
strftime()方法语法：
time.strftime(format[, t])
format -- 格式字符串。
t -- 可选的参数t是一个struct_time对象。
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身


time(...):返回当前时间的时间戳
localtime(...)：将一个时间戳转换成一个当前时区的struct_time
"""