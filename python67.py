#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

def inp(numbers,num):
    for i in range(num):
        numbers.append(int(raw_input('input a number:\n')))

def max_min(array,p):
    max = min =0
    for i in range(1,len(array) - 1):
        p = i 
        if array[p] > array[max]:max = p
        elif array[p] < array[min]:min = p
    k = max
    l = min
    array[0],array[k] = array[k],array[0]
    array[num - 1],array[l] = array[l],array[num - 1]

def outp(numbers):
    for i in range(len(numbers)):
        print numbers[i]

if __name__ == '__main__':
    array = []
    num = 4
    p = 0
    inp(array,num)
    max_min(array,p)
    outp(array)

