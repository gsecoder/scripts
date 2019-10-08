#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   54_generator.py
@Time    :   2019/10/8 14:59
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. 生成器
l1 = [x*x for x in range(10)]
print("列表生成式l1: ", l1)
g1 = (x*x for x in range(5))
print("生成器g1: ", g1)
try:
    print("生成器迭代值：", next(g1))
    print("生成器迭代值：", next(g1))
    print("生成器迭代值：", next(g1))
    print("生成器迭代值：", next(g1))
    print("生成器迭代值：", next(g1))
    print("生成器迭代值：", next(g1))
except StopIteration as e:
    print("生成器所有的值已经迭代结束了......")


# 2. 斐波拉契数列
# 0 1 1 2 3 5 8 13 21
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"


g = fib(5)
while True:
    try:
        x = next(g)
        print("......: ", x)
    except StopIteration as e:
        print("生成器已迭代完毕...", e.value)
        print("生成器已迭代完毕...", e.args)
        break
