#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   完全数.py
@Time    :   2020/1/22下午1:38
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备
数。例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余
3个数相加，
1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28
外，其余5个数相加，1+2+4+7+14=28。
那么问题来了，求1000以内的完全数有哪些？
"""

a = []

for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0 and j < i:
            s += j
    if i == s:
        print(i)
        a.append(i)

print("a: %s" % a)
