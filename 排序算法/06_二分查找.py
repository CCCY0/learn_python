#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cy
@contact: cccy0@foxmail.com
@file: test1.py
@time: 2018/6/1 12:28
@desc:
"""


def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


if __name__ == '__main__':
    li = [1, 2, 3, 6, 67, 89, 100]
    print(li)
    print(binary_search(li, 100))
    print(binary_search(li, 101))




