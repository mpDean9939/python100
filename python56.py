#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：用circle画圆形
"""

if __name__ == '__main__':
	from Tkinter import *

	# Canvas:画布
	"""
	w = Canvas ( master, option=value, ... )
	master:  这代表了父窗口.
	options: 下面是这个小工具最常用的选项列表。这些选项
	可以作为键 - 值对以逗号分隔.
	"""

	canvas = Canvas(width=800,height=600,bg='yellow')

	# 添加到主窗口
	canvas.pack(expand=YES,fill=BOTH)
	k = 1
	j = 1
	for i in range(0,26):
		# 在给定的坐标创建一个圆或椭圆。它的坐标两双。
		# 为椭圆的边界矩形左上角和底部右下角.
		canvas.create_oval(310-k,250-k,310+k,250+k,width=1)
		k += j
		j += 0.3

	mainloop()