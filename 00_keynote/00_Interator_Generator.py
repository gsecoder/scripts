#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   00_Interator_Generator.py
@Time    :   2019/9/22 12:07
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
# https://blog.csdn.net/iamlaosong/article/details/74908521
#     https://www.cnblogs.com/louyefeng/p/9430415.html
#   https://blog.csdn.net/m0_37870649/article/details/82749885
# 面试：https://blog.csdn.net/weixin_40449300/article/details/80384688

# Linux：https://www.cnblogs.com/gala1021/p/8519456.html
# git：https://segmentfault.com/a/1190000019315509?utm_source=tag-newest
#  https://blog.csdn.net/qq_36838191/article/details/80193693
# Jenkins：https://blog.csdn.net/zhuyb829/article/details/78899465
#

from collections.abc import Iterable, Iterator


# 1. 判断对象
string = 'test'
print("判断是否是可迭代对象：", isinstance(string, Iterable))
print("判断是否是迭代器：", isinstance(string, Iterator))


# 2. 迭代器的使用
list1 = range(10)
for i in list1:
    print("使用可迭代对象的方法", i)
print("********^^^^^^^^^^^**************")
# print("list1 iter is: ", iter(list1))
# print("list1 next is: ", next(list1))
# print("list1", list1.__iter__())
# print("list1", list1.__next__())      # list是可迭代对象，但是不是迭代器
#  将 "可迭代对象" 转换成 "迭代器对象"
r = iter(list1)
try:
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
    print("迭代器对象获取数据：", next(r))
except StopIteration as e:
    print("That is all folks!")


# 3. 生成器
list3 = [x*x for x in range(10)]
print("列表生成式list3：", list3)
generator_res = (x*x for x in range(5))
print("生成器generator_res：", generator_res)
try:
    print(next(generator_res))
    print(next(generator_res))
    print(next(generator_res))
    print(next(generator_res))
    print(next(generator_res))
    print(next(generator_res))
    print(next(generator_res))
    print(next(generator_res))
except StopIteration as e:
    print("生成器的值迭代结束了...")


# 斐波拉契数列
# 0 1 1 2 3 5 8
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"


for i in fib(5):
    print(i)
g = fib(5)
while True:
    try:
        x = next(g)
        print("generator: ", x)
    except StopIteration as e:
        print("生成器返回值：", e.value)
        print("生成器返回值：", e.args)
        break


# 4. 装饰器
