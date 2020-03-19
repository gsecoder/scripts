#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_protect.py
@Time    :   2019/10/14 17:37
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from threading import Thread


def run(name):
    time.sleep(2)
    print("%s is running..." % name)

def thread1():
    print(123)
    time.sleep(1)
    print("end123")

def thread2():
    print(456)
    time.sleep(0.5)
    print("end456")


if __name__ == "__main__":
    #t = Thread(target=run, args=("线程1", ))
    # # t.setDaemon(True) 等价于 t.daemon = True
    # # t.setDaemon(True)
    # t.daemon = True
    # t.start()
    # print("主进程")
    # print(t.is_alive())
    # 输出结果：
    # ---------------------因为主进程结束，守护主线程也就跟着结束了，所以不打印守护线程的语句
    # 主进程

    t1 = Thread(target=thread1)
    t2 = Thread(target=thread2)
    t1.daemon = True
    t1.start()
    t2.start()
    print("主进程2")


