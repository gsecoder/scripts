#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_ThreadPool_ProcessPool.py
@Time    :   2019/10/15 10:20
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import os
import random

def task(name):
    print("name: %s pid: %s run" % (name, os.getpid()))
    time.sleep(random.randrange(1, 3))


if __name__ == "__main__":
    # 设置最大同时运行的进程数
    # p = ProcessPoolExecutor(4)
    p = ThreadPoolExecutor(4)
    for i in range(10):
        # 异步提交任务，提交后不用管进程是否执行
        p.submit(task, '任务 %s' % i)
    # 将进程池的入口关闭，等待任务提交结束后才执行后面的任务, 默认wait=True
    p.shutdown(wait=True)
    print("主进程")
