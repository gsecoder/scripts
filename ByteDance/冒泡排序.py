#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   冒泡排序.py
@Time    :   2020/1/2119:25
@Author  :   crisimple
@Github :    https://juejin.im/user/5890963661ff4b006bebc3a5/posts
@Contact :   crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   a = [1, 3, 10, 9, 21, 35, 4, 6] 进行冒泡排序
"""

a = [1, 3, 10, 9, 21, 35, 4, 6]


def bubble_list(list_param):
    # 确定要循环的次数
    len_list_param = len(list_param)
    for i in range(len_list_param-1):
        count = 0
        for j in range(len_list_param-1-i):
            if list_param[j] > list_param[j+1]:
                list_param[j], list_param[j+1] = list_param[j+1], list_param[j]
                count += 1
        if count == 0:
            return list_param
    return list_param


print(bubble_list(a))

a.sort()
print(a)






