#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   202_timeit.py
@Time    :   2019/10/22 19:27
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
#   Timer是测量小段代码执行速度的类。
#   stmt参数是要测试的代码语句（statment）；
#   setup参数是运行代码时需要的设置；
#   timer参数是一个定时器函数，与平台有关
# timeit.Timer.timeit(number=1000000)
#   Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。方法返回执行代码的平均耗时，一个float类型的秒数。


def test1():
    l1 = []
    for i in range(1000):
        l1 = l1 + [i]

def test2():
    l2 = []
    for i in range(1000):
        l2.append(i)

def test3():
    l3 = [i for i in range(1000)]

def test4():
    l4 = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "seconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "seconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "seconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "seconds")


# pop内置函数的测试
#  pop最后一个元素的效率远远高于pop第一个元素
x = list(range(2000000))
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero ", pop_zero.timeit(number=1000), "seconds")
x = list(range(2000000))
pop_end = Timer("x.pop()", "from __main__ import x")
print("pop_end ", pop_end.timeit(number=1000), "seconds")
