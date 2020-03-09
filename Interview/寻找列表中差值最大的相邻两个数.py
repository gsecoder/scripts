#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   寻找列表中差值最大的相邻两个数.py
@Time    :   2020/2/28上午10:58
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   输入列表和列表中元素的个数，返回列表中差值最大的两个数
"""

a1 = [9, 3, 1, 10]
b1 = 4

a2 = [5, 5, 5, 5]
b2 = 4


def findMaxDivision(A, n):
    # 先将列表排序
    A.sort()
    # 定义最小的负数
    maxx = -0x3f3f3f3f
    #
    for i in range(1, n):
        if abs(A[i-1] - A[i]) > maxx:
            maxx = abs(A[i-1] - A[i])

    return maxx


print(findMaxDivision(a1, b1))
