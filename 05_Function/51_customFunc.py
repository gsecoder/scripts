#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   51_customFunc.py
@Time    :   2019/7/23 10:05
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# here put the import lib
# 函数的定义：函数是一段组织好的，可多次重复使用的，用来实现单一或相关功能的代码段。

# 1.语法
# 自定义函数
def custom_func(elem):
    print("这是我的自定义函数...")
    print("我是参数elem: ", elem)


# 函数调用
custom_func(1)


# -------------
# 2. 函数的参数
# 2.1 普通参数
def common_parameter(par1, par2):       # 函数定义，形参，提供给使用者一个接口
    print(par1)
    print(par2)


common_parameter(11, 22)    # 函数调用，实参，实参值传递给形参

# 2.2 默认参数
# par_default为函数的默认参数，函数调用时如果不传值的话，就是用默认的参数的值；如果传值了就用传的值
def default_parameter(par1, par2, par_default="我是默认值"):
    print("..........default parameter..........")
    print(par1)
    print(par2)
    print(par_default)


default_parameter("我是par1", 222)
default_parameter(111, 222, "test")
default_parameter(par_default="位置参数生效", par1=1111, par2=True)

# 2.3 动态参数
# (1) 可以接受任意个参数
# (2) 动态参数有两种：*args和**kwargs，*args必须在*kwargs的前面
#       *args: 接受的是按照位置传参的值，组织成一个 **元组**
#       **kwargs: 接受的是按照关键字传参的值，组成一个 **字典**
# (3) 参数的传递顺序：位置参数、*args、默认参数、**kwargs
def dynamic_parameter(par1, par2, *args, par_default="default", **kwargs):
    print(".......dynamic parameter.......")
    print(par1)
    print(par2)
    print(args)
    print(par_default)
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])


dynamic_parameter(1, 2, 2, 3, 4, 5, par_default=5, name='kwargs', age=12)


# 3. 函数的返回值
# return 语句用于退出函数，选择性地向调用方式返回一个表达式。不带参数值的return语句返回None。
def return_func(a, b):
    total = a + b
    print("函数内：", total)
    return total


total_exc = return_func(12, 23)
print("函数外：", total_exc)
