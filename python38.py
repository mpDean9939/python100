#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将
a[i][i]累加后输出。
"""

# 得到矩阵a
def inputMatrix(N):
	a = []
	for i in range(N):
		a.append([]) # 每一行作为一项
		for j in range(N):
			a[i].append(float(raw_input('Input the a[%d][%d]:\n' % (i,j))))
	getSum(a,N)

#求对角线元素之和
def getSum(a,N):
	sum = 0.0
	for i in range(N):
		sum += a[i][i]
	print u'矩阵a的正对角线的所有元素之和为：'.encode('gbk'),sum

def main():
	inputMatrix(3)

if __name__ == '__main__':
	main()