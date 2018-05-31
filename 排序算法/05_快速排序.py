#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cy
@contact: cccy0@foxmail.com
@file: test1.py
@time: 2018/5/31 12:28
@desc:
"""


def quick_sort(alist, first, last):
    """快速排序"""
    # 递归停止条件
    if first >= last:
        return

    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high 左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        # low 右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 此时 low == high
    alist[low] = mid_value

    # low 左边的列表排序
    quick_sort(alist, first, low-1)
    # low 右边的列表排序
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    li = [56, 754, 23, 565, 3434, 245, 78]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)




