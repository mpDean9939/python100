#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：找到年龄最大的人，并输出。
"""

if __name__ == '__main__':
	person = {"li":18,"wang":34,"zhang":34}
	m = 'li'
	for key in person.keys():
		if person[m] < person[key]:
			m = key

	print '%s,%d' % (m,person[m])
