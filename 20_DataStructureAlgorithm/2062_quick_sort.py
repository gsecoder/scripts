#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2062_quick_sort.py
@Time    :   2019/10/24 15:49
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""快速排序
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(n**2)
"""

def quick_sort(alist, start, end):

    # 递归的退出条件
    if start >= end:
        return

    # 设置其实元素为基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素饭到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准位置元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


if __name__ == "__main__":
    alists = [54,26,93,17,77,31,44,55,20]
    quick_sort(alists, 0, len(alists)-1)
    print(alists)
