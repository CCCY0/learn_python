#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cy
@contact: cccy0@foxmail.com
@file: test1.py
@time: 2018/5/31 12:28
@desc:
"""


def bubble_sort(alist):
    """冒泡排序"""
    for j in range(0, len(alist)-1):
        count = 0
        for i in range(0, len(alist)-1-j):
            # 依次判断
            if alist[i] > alist[i+1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            # 如果从来没有进行过交换,说明本来就是有序数列
            return


if __name__ == '__main__':
    li = [56, 754, 23, 565, 3434, 245, 78]
    print(li)
    bubble_sort(li)
    print(li)




