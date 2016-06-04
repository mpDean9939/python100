#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数
（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来
第几号的那位。
"""

if __name__ == '__main__':
	n = int(raw_input('input the total numbel:\n'))
	num = []
	for i in range(n):
		num.append(i + 1)

	i = 0
	k = 0
	m = 0

#总体思路就是把报数是3的num列表元素全部设为0，最后判断哪个不是0哪个就是最后剩下的
	while m < n - 1: # 这里的m是设为0的数目，从0开始一共n-1个
		if num[i] != 0: k += 1
		if k == 3:
			num[i] = 0
			k = 0
			m += 1
		i += 1
		if i == n: i = 0

	i = 0
	while num[i] == 0: i += 1
	print num[i]