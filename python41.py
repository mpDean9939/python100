#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：模仿静态变量的用法。
"""

def varfunc():
	var = 0
	print 'var = %d' % var # 0,0,0
	var += 1

if __name__ == '__main__':
	for i in range(3):
		varfunc()

class Static:
	StaticVar = 5
	def varfunc(self):
		self.StaticVar += 1
		print self.StaticVar

print Static.StaticVar # 5
a = Static()
for i in range(3):
	a.varfunc()