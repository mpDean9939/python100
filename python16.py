#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
datetime:datetime是date与time的结合体，包括date与time的所有信息。
它的构造函数如下：  
 datetime. datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )  
 各参数的含义与date、time的构造函数中的一样，要注意参数值的范围。
"""

if __name__=='__main__':

	#输出今日日期，格式为dd/mm/yyyy
	print(datetime.date.today().strftime('%d/%m/%Y'))

	#创建日期对象
	myBirthDate = datetime.date(1941,1,5)
	print(myBirthDate.strftime('%d/%m/%Y'))

	#日期算术运算,timedelta表示时间间隔，+表示时间前进，-表示后退
	myBirthDate = myBirthDate + datetime.timedelta(days=1)
	print(myBirthDate.strftime('%d/%m/%Y'))

	#日期替换
	myBirthDate = myBirthDate.replace(year=myBirthDate.year + 1)
	print(myBirthDate.strftime('%d/%m/%Y'))