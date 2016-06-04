#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：两个乒乓球队进行比赛，各出三人。甲队
为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，
c说他不和x,z比，请编程序找出三队赛手的名单。
程序分析：需要注意，任何一人都只能和一个人匹配进行比赛
"""

#实际上只做了两件事，第一，避免重复，第二，匹配条件
def findName():
	for a in range(ord('x'),ord('z') + 1):
	    for b in range(ord('x'),ord('z') + 1):
	        if a != b:#这里的目的是：一旦a和x,y,z其中之一匹配了，那么b就不能再和之匹配，x,y,z中任何一个不能同时跟两个人匹配比赛
	            for c in range(ord('x'),ord('z') + 1):
	                if (a != c) and (b != c):#这里也一样，避免重复
	                    if (a != ord('x')) and (c != ord('x')) and (c != ord('z')):
	                    	print 'order is a -- %s\t b -- %s\tc--%s' % (chr(a),chr(b),chr(c))

def main():
	findName()
	
if __name__ == '__main__':
	main()
