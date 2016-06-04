#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，
则判断用情况语句或if语句判断第二个字母。。
要求复杂了可以加入大小写字母转换
"""
def weekJudge():
	letter = raw_input('Please input the first word:')

	if letter == 'M' or 'm':
		print 'Monday'

	elif letter == 'T' or 't':
		print 'Please input the twice word:'
		letter = raw_input('Please input:')

		if letter == 'u' or 'U':
			print 'Tuesday'
		elif letter == 'h' or 'H':
			print 'Thusday'
		else:
			print 'data error'

	elif letter == 'W' or 'w':
		print 'Wednesday'

	elif letter == 'F' or 'f':
		print 'Friday'

	elif letter == 'S' or 's':
		print 'Please input the twice word:'
		letter = raw_input('Please input:')

		if letter == 'u' or 'U':
			print 'Sunday'
		elif letter == 'a' or 'A':
			print 'Saturday'
		else:
			print 'data error'

def main():
	weekJudge()

if __name__ == '__main__':
	main()
