#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   71_Process_protect.py
@Time    :   2019/10/11 12:54
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from multiprocessing import Process
import time
import os


def task1(name, n):
    print("%s id: %s is running..., parent id is <%s>" % (name, os.getpid(), os.getppid()))
    time.sleep(n)
    print("%s id: %s has done===, parent id is <%s>" % (name, os.getpid(), os.getppid()))
    # 字进程不允许创建子进程
    # p = Process(target=time.sleep, args=(2, 3))
    # p.start()


def task2(name, n):
    print("%s id: %s is running..., parent id is <%s>" % (name, os.getpid(), os.getppid()))
    time.sleep(n)
    print("%s id: %s has done===, parent id is <%s>" % (name, os.getpid(), os.getppid()))


if __name__ == "__main__":
    p_task1 = Process(target=task1, args=("task1", 3))
    p_task2 = Process(target=task2, args=("task2", 3))
    #一定要在p.start()前设置, 设置p为守护进程, 禁止p创建子进程, 并且父进程代码执行结束, p即终止运行
    p_task1.daemon = True
    # 未加守护进程的任务还会继续运行
    p_task1.start()
    p_task2.start()
    print("主程序%s......")
