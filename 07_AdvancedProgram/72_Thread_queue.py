#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_queue.py
@Time    :   2019/10/14 21:27
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import queue


# 1. 先进先出
first_in_first_out = queue.Queue(5)
first_in_first_out.put('first')
first_in_first_out.put(2)
first_in_first_out.put('third')
# block = True时阻塞，timeout=3，等待三秒后如果还没有从里面取出数据，则阻塞
first_in_first_out.put(4, block=True, timeout=3)
print(first_in_first_out.get())
print(first_in_first_out.get())
print(first_in_first_out.get())
print(first_in_first_out.get(block=False))
print("\n")


# 2. 后进先出
last_in_first_out = queue.LifoQueue(3)
last_in_first_out.put("L1")
last_in_first_out.put("L2")
last_in_first_out.put("L3")
print(last_in_first_out.get())
print(last_in_first_out.get())
print(last_in_first_out.get())
print("\n")


# 3. 优先级队列（存储数据时可设置优先级的队列）
priority = queue.PriorityQueue(3)
priority.put((10, 'one'))
priority.put((40, 'two'))
priority.put((20, 'three'))
print(priority.get())
print(priority.get())
print(priority.get())
