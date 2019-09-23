#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   01_Sorting.py
@Time    :   2019/9/22 18:25
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""


class SortMethod(object):
    # 插入排序
    def insert_sort(self, lists):
        count = len(lists)
        for i in range(1, count):
            key = lists[i]
            j = i -1
            while j >= 0:
                if lists[j] > key:
                    lists[j + 1] = lists[j]
                    lists[j] = key
                j -= 1
        return lists

    # 希尔排序
    def shell_sort(self, lists):
        pass

    # 冒泡排序
    def bubble_sort(self, lists):
        pass

    # 快速排序
    def quick_sort(self, lists):
        pass

    # 直接排序
    def select_sort(self, lists):
        pass

    # 堆排序
    def heap_sort(self, lists):
        pass

    # 归并排序
    def merge_sort(self, lists):
        pass