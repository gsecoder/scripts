#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2061_bubble_sort.py
@Time    :   2019/10/24 12:57
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""冒泡排序
最优时间复杂度：O(n)
最坏时间复杂度：O(n**2)
"""
def bubble_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)
