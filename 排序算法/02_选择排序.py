#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cy
@contact: cccy0@foxmail.com
@file: test1.py
@time: 2018/5/31 12:28
@desc:
"""


def select_sort(alist):
    """选择排序"""
    for j in range(0, len(alist)-1):
        min_index = j
        for i in range(j+1, len(alist)):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    li = [56, 754, 23, 565, 3434, 245, 78]
    print(li)
    select_sort(li)
    print(li)




