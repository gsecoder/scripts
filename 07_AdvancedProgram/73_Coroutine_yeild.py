#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   73_Coroutine_yeild.py
@Time    :   2019/10/15 12:38
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import time

def task1(name):
    for i in range(3):
        print("%s is running...%s" % (name, i))
        yield
        time.sleep(1)

def task2(name):
    for i in range(3):
        print("%s is running...%s" % (name, i))
        yield
        time.sleep(1)

def main():
    g1 = task1('任务1')
    g2 = task2('任务2')
    for i in range(3):
        next(g1)
        next(g2)
    print("执行完毕")


if __name__ == "__main__":
    main()
