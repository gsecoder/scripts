#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   阶乘计算.py
@Time    :   2020/1/22下午1:46
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from functools import reduce

a = 3
b = reduce(lambda x, y: x*y, range(1, a+1))
print(b)


def digui(n):
    if n == 1:
        return 1
    else:
        return n * digui(n-1)


print(digui(a))


# 解决idea大边框问题：https://blog.csdn.net/ysy950803/article/details/102492124（decorate）
# https://gitee.com/liuzy1988/MyLinux/blob/master/Deepin_15.11.md