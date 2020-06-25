#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : used_sort.py
__time__    : 2020/6/23 23:27
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__resume__ : 冒泡排序
"""

"""
    冒泡排序：一次比较两个元素
        外层循环控制要排序列表的循环次数
        内层循环控制剩余元素还需要比较的次数
        时间复杂度最优为：O(n)
        最坏的时间复杂度：O(n^2)
"""
def bubble_sort(args_list):
    for i in range(len(args_list)):
        for j in range(len(args_list) - i - 1):
            if args_list[j] > args_list[j+1]:
                args_list[j], args_list[j+1] = args_list[j+1], args_list[j]
    return args_list

def bubble_sort1(args_list):
    for i in range(len(args_list) - 1):
        for j in range(len(args_list) - i - 1):
            if args_list[j] > args_list[j+1]:
                args_list[j], args_list[j+1] = args_list[j+1], args_list[j]

    return args_list

"""
    选择排序：在未排序序列中找到最小（大）的元素，存放到排序序列的起始位置
        然后在未排序的元素中继续找寻最小（大）的元素，然后放在已排序序列的末尾
    时间最优复杂度：O(n^2)
    时间最坏复杂度：O(n^2)
"""
def select_sort(args_list):
    for i in range(0, len(args_list)):
        min_num = i
        for j in range(i+1, len(args_list)):
            if args_list[j] < args_list[min_num]:
                min_num = j
        args_list[i], args_list[min_num] = args_list[min_num], args_list[i]
    return args_list

def select_sort1(args_list):
    for i in range(len(args_list)):
        min_num = i
        for j in range(i+1, len(args_list)):
            if args_list[j] < args_list[min_num]:
                min_num = j
        args_list[i], args_list[min_num] = args_list[min_num], args_list[i]
    return args_list

if __name__ == '__main__':
    list_sample = [2, 1, 4, 6, 3, 10, 9]

    # print(bubble_sort(list_sample))

    # print(select_sort(list_sample))

    # print(bubble_sort1(list_sample))

    print(select_sort1(list_sample))