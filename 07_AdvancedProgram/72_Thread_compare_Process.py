#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_compare_Process.py
@Time    :   2019/10/14 10:56
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from multiprocessing import Process
# 1. 开启速度
# 1.1 在主进程下开启线程
from threading import Thread


def run(name):
    print("%s thread is running..." % name)
    time.sleep(2)
    print("%s thread run done===" % name)

# 1.2 在主进程下开启子进程
def child_process(name):
    print("%s process is running..." % name)
    time.sleep(2)
    print("%s process run done===" % name)


# 2.pid不同
# 2.1 在主进程下开启多个线程，每个线程都跟主进程的pid一样【pid（process id：进程的id号）】
import os

def pid_thread_task(name):
    # 一个进程内多个线程是平级别的
    print("%s 子进程：%s" % (name, os.getpid()))

# 2.2 开多个进程，每个进程都有不同的pid
def pid_process_task(name):
    print("%s 子进程的pid: %s, 父进程的pid: %s" %(name, os.getpid(), os.getppid()))


# 3.同一进程内的多个线程共享该进程的地址空间，父进程与子进程不共享地址空间，进程之间的地址空间是隔离的
n = 100
def task3(name, num1):
    global n
    n = 0
    print("=====%s=====" % name)
    n = n + num1
    print("-----%s-----" % n)


if __name__ == "__main__":
    # 1.1
    # t1 = Thread(target=run, args=('主进程下的线程', ))
    # t1.start()
    # print("\n主进程下有线程")

    # # 1.2
    # p1 = Process(target=child_process, args=("主进程下的进程", ))
    # p1.start()
    # print("\n主进程下有子进程")

    # 2.1
    # pid_thread_task_1 = Thread(target=pid_thread_task, args=(' 线程1', ))
    # pid_thread_task_2 = Thread(target=pid_thread_task, args=(' 线程2', ))
    # pid_thread_task_1.start()
    # pid_thread_task_2.start()
    # print("\n 2.1的主进程：", os.getpid())

    # 2.2
    # pid_process_task_1 = Process(target=pid_process_task, args=(' 进程1', ))
    # pid_process_task_2 = Process(target=pid_process_task, args=(' 进程1', ))
    # pid_process_task_1.start()
    # pid_process_task_2.start()
    # print("\n 2.2的主进程：", os.getpid())

    # 3
    p3 = Process(target=task3, args=("进程31", 100))
    t31 = Thread(target=task3, args=("线程31", 100))
    t32 = Thread(target=task3, args=("线程32", 200))
    # p3.start()
    # p3.join()
    t31.start()
    t32.start()
    print("\n\n【p3主进程】", n)

