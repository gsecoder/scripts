#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   52_exceptionHanding.py
@Time    :   2019/8/15 18:15
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. try...exception...finally异常处理
list_exception = [1, 2, 3]

try:
    for i in list_exception:
        print(list_exception[i+2])
except IndexError as e:
    print("异常 %s 已经在这里被捕获了，下面再有异常处理就不再被捕获了" % e)
except Exception as e:
    print(e)
finally:
    print("程序执行结束，不管异常是否被捕获，这里一定始终会执行")

