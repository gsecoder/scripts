#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_Asynchronous_call_recall.py
@Time    :   2019/10/15 11:12
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from concurrent.futures import ThreadPoolExecutor

import random


def swim(name):
    print("%s is swimming" % name)
    time.sleep(random.randint(1, 5))
    swim_len = random.randint(10, 20)
    return {"name": name, 'swim_len': swim_len}

def distance(swim_res):
    # swim_res = swim_res.result()
    name = swim_res['name']
    s_length = swim_res['swim_len']
    print("%s 游了 %s km" % (name, s_length))


if __name__ == '__main__':
    # 1. 同步调用
    pool = ThreadPoolExecutor(13)
    swim_res1 = pool.submit(swim, 'A').result()
    distance(swim_res1)
    swim_res2 = pool.submit(swim, 'B').result()  # result取得结果
    distance(swim_res2)
    swim_res3 = pool.submit(swim, 'C').result()
    distance(swim_res3)

    # 2. 异步调用
    # pool = ThreadPoolExecutor(13)
    # pool.submit(swim, 'AA').add_done_callback(distance)
    # pool.submit(swim, 'BB').add_done_callback(distance)
    # pool.submit(swim, 'CC').add_done_callback(distance)

print("#############################")
