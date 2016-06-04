#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：有一分数序列：2/1，3/2，5/3，8/5，
13/8，21/13...求出这个数列的前20项之和。
程序分析：注意分子与分母的变化规律。把分数分为
两部分看，分子和分母分成两个单独的数来对待
"""

#方法一
def fractionRule(n):
	denominator = 1.0
	molecule = 2.0
	sum = 0
	for i in range(1,n+1):
		sum += molecule / denominator
		temp = molecule
		molecule = molecule + denominator
		denominator = temp
	print u'这个数列的前%d项的和为：%f'.encode('gbk') % (n,sum)

#方法二  函数式lambda编程
def fractionRuleLambda(n):
	denominator = 1.0
	molecule = 2.0
	l = []
	for j in range(1,n+1):
		denominator,molecule = molecule,molecule+denominator
		l.append(molecule / denominator)
	print u'这个数列的前%d项的和为：%f'.encode('gbk') % (n,reduce(lambda x,y:x + y,l))

def  main():
	fractionRule(20)
	fractionRuleLambda(20)

if __name__ == '__main__':
	main()
