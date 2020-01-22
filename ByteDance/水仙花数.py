#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   水仙花数.py
@Time    :   2020/1/22下午1:29
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   打印出100-999所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋
5的三次方＋3的三次方。
"""

# sxh = []
# for i in range(100, 1000):
#     s = 0
#     m = list(str(i))
#     for j in m:
#         s += int(j)**len(m)
#     if i == s:
#         print(i)
#         sxh.append(i)
# print("sxh: %s" % sxh)


sxh = []
for i in range(100, 1000):
    m = list(list(str(i)))
    s = 0
    for j in m:
        s += int(j)**len(m)
    if i == s:
        print(i)
        sxh.append(i)

print("sxh: %s" % sxh)