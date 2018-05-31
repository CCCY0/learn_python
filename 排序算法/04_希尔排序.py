#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cy
@contact: cccy0@foxmail.com
@file: test1.py
@time: 2018/5/31 12:28
@desc:
"""


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap > 0:
        # 插入算法,以gap步长为单位
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap
        gap //= 2


if __name__ == '__main__':
    li = [56, 754, 23, 565, 3434, 245, 78]
    print(li)
    shell_sort(li)
    print(li)




