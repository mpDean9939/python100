#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：画图，学用line画直线。
"""

if __name__ == '__main__':
	from Tkinter import *

	canvas = Canvas(width=600,height=600,bg='green')
	canvas.pack(expand=YES,fill=BOTH)

	x0 = 50
	y0 = 100
	x1 = 50
	y1 = 200
	for i in range(3):
		canvas.create_line([x0,y0],[x0,y1],width=3,fill='black')
		x0 = x0 - 15
		y0 = y0 - 15
		x1 = x1 + 15
		y1 = y1 + 15

	x0 = 263
	y1 = 275
	y0 = 263
	for i in range(5):
		canvas.create_line(x0,y0,x0,y1,fill='red')
		x0 += 5
		y0 += 5
		y1 += 5

	mainloop()