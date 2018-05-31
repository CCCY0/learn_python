#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cy
@contact: cccy0@foxmail.com
@file: test1.py
@time: 2018/5/31 12:28
@desc:
"""


def insert_sort(alist):
    """插入排序"""
    for j in range(1, len(alist)):
        i = j
        # 取元素, 插入到前面的正确位置
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [56, 754, 23, 565, 3434, 245, 78]
    print(li)
    insert_sort(li)
    print(li)




