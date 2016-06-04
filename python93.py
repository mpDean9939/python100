#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
时间函数举例三
"""

if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(3000):
        print i
    end = time.clock()
    print 'different is %6.3f' % (end - start)