#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   71_Process_join.py
@Time    :   2019/10/10 23:38
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import time
from multiprocessing import Process

import os


def join_task(name):
    print("%s id: %s is running..., parent id is <%s>" % (name, os.getpid(), os.getppid()))
    time.sleep(3)
    print("%s id: %s has done===, parent id is <%s>" % (name, os.getpid(), os.getppid()))

# join并发
def join_concurrent(name, n):
    print("---%s id: %s is running..., parent id is <%s>---" % (name, os.getpid(), os.getppid()))
    time.sleep(n)
    # print("---%s id: %s has done===, parent id is <%s>---" % (name, os.getpid(), os.getppid()))

# join串行
def join_serial(name, n):
    print("$$$%s id: %s is running..., parent id is <%s>$$$" % (name, os.getpid(), os.getppid()))
    time.sleep(n)
    print("$$$%s id: %s has done===, parent id is <%s>$$$" % (name, os.getpid(), os.getppid()))


n = 100

# 进程之间的空间是隔离的
def spatial_isolation():
    global n
    n = 0
    print("子进程内的n: ", n)


if __name__ == "__main__":
    # join检测子进程
    p_task = Process(target=join_task('task进程'), name="自定义的进程的名称")
    p_task.start()
    # 加入join方法后一定会等到子进程结束以后才会执行主进程
    print("子进程存活状态：", p_task.is_alive())
    p_task.join()
    print("子进程存活状态：", p_task.is_alive())
    print("主进程的id：%s, 及父进程的id：%s" % (os.getpid(), os.getppid()))
    print("验证了存在僵尸进程：", p_task.pid)
    print("子进程的名称：", p_task.name)

    # join并发
    start_time_concurrent = time.time()
    p_concurrent_1 = Process(target=join_concurrent, args=('join并发1', 3))
    p_concurrent_2 = Process(target=join_concurrent, args=('join并发2', 2))
    p_concurrent_3 = Process(target=join_concurrent, args=('join并发3', 3))
    p_concurrent_1.start()
    p_concurrent_2.start()
    p_concurrent_3.start()
    # 三个是以并发进行的，只是等待最长的程序执行完毕才算结束
    p_concurrent_1.join()
    p_concurrent_2.join()
    p_concurrent_3.join()
    print("join并发主进程总耗时：", (time.time() - start_time_concurrent))

    # join串行
    start_time_serial = time.time()
    p_serial_1 = Process(target=join_concurrent, args=('join串行1', 3))
    p_serial_2 = Process(target=join_concurrent, args=('join串行2', 2))
    p_serial_3 = Process(target=join_concurrent, args=('join串行3', 1))
    # 每个都是执行完以后再进行下一步
    p_serial_1.start()
    p_serial_1.join()
    p_serial_2.start()
    p_serial_2.join()
    p_serial_3.start()
    p_serial_3.join()
    print("join串行主进程总耗时：", (time.time() - start_time_serial))

    # 进程之间的空间是隔离的
    p_spatial_isolation = Process(target=spatial_isolation)
    p_spatial_isolation.start()
    print('主进程内n: ', n)

