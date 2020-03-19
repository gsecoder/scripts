#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread.py
@Time    :   2019/10/12 12:18
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from threading import Thread

import random


def thread_one(name):
    print("%s is running." % name)
    time.sleep(random.randrange(1, 3))
    print("%s run end====" % name)


class ThreadTwo(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s is running..." % self.name)
        time.sleep(random.randrange(1, 3))
        print("%s run end two====" % self.name)


if __name__ == "__main__":
    # 创建线程第一种方式
    to = Thread(target=thread_one, args=("第一种创建线程的方式...", ))
    to.start()
    print("主线程一")

    # 创建线程第二种方式
    tt = ThreadTwo('第二种创建线程的方式...')
    tt.start()
    print("主线程二")
