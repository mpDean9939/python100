#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加
由键盘控制。
程序分析：关键是计算出每一项的值。
"""

Tn = 0
Sn = []
n = int(raw_input('repeat time n = :\n'))
a = int(raw_input('repeat num a = :\n'))
for count in range(n):
	Tn = Tn + a
	a = a * 10
	Sn.append(Tn)
	print Tn

Sn = reduce(lambda x,y:x + y,Sn)
print Sn
"""
python中的reduce内建函数是一个二元操作函数，他用来
将一个数据集合（链表，元组等）中的所有数据进行下列操
作：用传给reduce中的函数 func()（必须是一个二元操
作函数）先对集合中的第1，2个数据进行操作，得到的结果再
与第三个数据用func()函数运算，最后得到一个结果。
"""