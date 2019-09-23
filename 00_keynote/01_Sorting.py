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

    def __init__(self, lists):
        self.lists = lists

    # 插入排序
    def insert_sort(self):
        n = len(self.n)
        for ii in range(1, n):
            key = self.lists[ii]
            j = ii - 1
            while j >= 0:
                if self.lists[j] > key:
                    self.lists[j + 1] = self.lists[j]
                    self.lists[j] = key
                j -= 1
        return self.lists

    # 希尔排序
    def shell_sort(self, lists):
        pass

    # 冒泡排序
    def bubble_sort(self):
        # 计算列表的长度
        n = len(self.lists)
        arr_b = []
        # 循环遍历列表
        for bi in range(n):
            for j in range(0, n-bi-1):
                if self.lists[j] > self.lists[j+1]:
                    self.lists[j], self.lists[j+1] = self.lists[j+1], self.lists[j]
            # print(self.lists)
        print(self.lists)


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


if __name__ == "__main__":
    bubble_lists = [3, 1, 5, 2, 6, 0]
    sm = SortMethod(bubble_lists)
    sm.bubble_sort()
    # arr = []
    # for i in range(len(bubble_lists)):
    #     arr.append(i)
    # print(arr)