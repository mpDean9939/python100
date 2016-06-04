#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：海滩上有一堆桃子，五只猴子来分。第一只猴子
把这堆桃子平均分为五份，多了一个，这只猴子把多的
一个扔入海中，拿走了一份。第二只猴子把剩下的桃子
又平均分成五份，又多了一个，它同样把多的一个扔入
海中，拿走了一份，第三、第四、第五只猴子都是这样
做的，问海滩上原来最少有多少个桃子？
"""

if __name__ == '__main__':
	i = 0
	j = 1
	sumAll = 0
	while (i < 5):
		sumAll = 4 * j
		for i in range(0,5):
			if(sumAll % 4 != 0):
				break
			else:
				i += 1
			sumAll = (sumAll / 4) * 5 + 1
		j += 1
	print sumAll