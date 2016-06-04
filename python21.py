#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，
当即吃了一半，还不瘾，又多吃了一个第二天早上又
将剩下的桃子吃掉一半，又多吃了一个。以后每天早上
都吃了前一天剩下的一半零一个。到第10天早上想再吃时，
见只剩下一个桃子了。求第一天共摘了多少。
程序分析：采取逆向思维的方法，从后往前推断
"""

def eatPeach(alldays):
	balance = 1 #第10天的剩余量
	for day in range(alldays,1,-1):
		y = (balance + 1) *2
		balance = y
	return y

def main():
	print eatPeach(10)

if __name__ == '__main__':
	main()