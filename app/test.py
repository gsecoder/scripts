#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py
@Time    :   2019/10/24 16:47
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

def quick_sort(alist, start, end):

    # 递归退出条件
    if start > end:
        return

    # 确定基准元素
    mid = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        while low<high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    # 分别递归基准值左右的子序列
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

alists = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alists, 0, len(alists)-1)
print(alists)
