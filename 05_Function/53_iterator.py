#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   53_iterator.py
@Time    :   2019/10/8 11:23
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. 判断可迭代对象
from collections.abc import Iterable, Iterator

string1 = "Iterable"
list1 = range(10)
if isinstance(string1, Iterable):
    print("该对象是可迭代对象")
elif isinstance(string1, Iterator):
    print("该对象是迭代器")
else:
    print("您的判断不存在")


# 2. 迭代对象的使用
list1 = range(5)
for i in list1:
    print(i)
# 将 "可迭代对象" 转换成 "迭代器对象"
if isinstance(list1, Iterable):
    print("该对象是可迭代对象")
elif isinstance(list1, Iterator):
    print("该对象是迭代器")
else:
    print("您的判断不存在")
list2 = iter(list1)
try:
    print("迭代器对象获取数据：", next(list2))
    print("迭代器对象获取数据：", next(list2))
    print("迭代器对象获取数据：", next(list2))
    print("迭代器对象获取数据：", next(list2))
    print("迭代器对象获取数据：", next(list2))
    print("迭代器对象获取数据：", next(list2))
except StopIteration as e:
    print("That is all folks!")


