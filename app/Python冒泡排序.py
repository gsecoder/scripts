#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Python冒泡排序.py
@Time    :   2019/10/17 17:33
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# def bubble_sort(args):
#     n = len(args)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if args[j] > args[j+1]:
#                 args[j], args[j+1] = args[j+1], args[j]

def bubble_sort(args):
    n = len(args)
    for i in range(n):
        for j in range(n-i-1):
            if args[j] > args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))

