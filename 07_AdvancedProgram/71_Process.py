#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   71_Process.py
@Time    :   2019/10/10 21:02
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from multiprocessing import Process
import time
import random
import os


def task(name):
    print("%s is running..." % name)
    time.sleep(random.randrange(1, 5))
    print("%s is done..." % name)


# 第二种创建子进程的方法
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()  # 将父类的功能进行重用
        self.name = name

    # start将调用这个run方法
    def run(self) -> None:
        print("%s %s is running..., parent id is %s" % (self.name, os.getpid(), os.getppid()))
        time.sleep(3)
        print("%s %s is done-----, parent id is %s" % (self.name, os.getpid(), os.getppid()))


if __name__ == "__main__":
    # 第一种方式
    p1 = Process(target=task, args=("A", ))
    p2 = Process(target=task, args=("B", ))
    p3 = Process(target=task, args=("C", ))
    p4 = Process(target=task, args=("D", ))
    # 只是给操作系统发送了一个信号，由操作系统将父进程地址空间中的数据拷贝给子进程，作为子进程运行的初始状态，开启后再运行task
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主1......', os.getpid(), os.getppid())
    # 执行结果：执行结果因为执行进程会有一段时间，所以先做打印操作
    # --------------------
    # 主
    # 任务名称 is running...
    # 任务名称 is done...
    p = MyProcess('子进程2')
    p.start()
    # os.getpid() --- 查看子进程的id
    # os.getppid() --- 查看父进程的id
    print('主2......', os.getpid(), os.getppid())

