#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_methods.py
@Time    :   2019/10/14 16:42
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from threading import Thread, currentThread, active_count, enumerate


def task():
    # 获取当前线程的名字
    print("%s is running" % currentThread().getName())
    time.sleep(1)
    print("%s is done ======" % currentThread().getName())


if __name__ == "__main__":
    t = Thread(target=task, name='子线程1')
    t.start()
    t.setName("改名为新线程名称1")
    t.join()
    print("新的子线程的名称为：", t.getName())
    print("线程是否存活：", t.isAlive())

    currentThread().setName("主线程新名字")
    print("主线程的名字：", currentThread().getName())
    print("线程是否存活：", t.isAlive())
    t.join()
    print("查看活跃的线程数：", active_count())
    print("将当前活跃的线程显示出来：", enumerate())
