#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_lock.py
@Time    :   2019/10/14 19:28
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from threading import Thread, Lock

n1 = 100
n2 = 100

def unlock_task():
    # 未加锁之前
    global n1
    temp = n1
    # 未加锁之前，100个线程都停留在这并且temp都等于100
    time.sleep(0.1)
    n1 = temp - 1

def lock_task():
    global n2
    # 开始加锁
    mutex.acquire()
    temp = n2
    time.sleep(0.1)
    n2 = temp - 1
    # 解锁
    mutex.release()


if __name__ == "__main__":
    # 未加锁之前
    t_1 = []
    for i in range(100):
        t = Thread(target=unlock_task)
        t_1.append(t)
        t.start()
    for t in t_1:
        t.join()
    print('未加锁的主进程', n1)
    # ----- 执行结果 -----
    # 主进程 100

    # 加锁
    mutex = Lock()
    t_2 = []
    for i2 in range(100):
        t2 = Thread(target=lock_task)
        t_2.append(t2)
        t2.start()
    for t2 in t_2:
        t2.join()
    print("加锁后的主进程", n2)
