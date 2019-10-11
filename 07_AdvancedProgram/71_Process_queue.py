#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   71_Process_queue.py
@Time    :   2019/10/11 19:50
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from multiprocessing import Process, Queue

q = Queue(3)

q.put(1)
q.put(2)
print("当前队列是否已满：", q.full())
q.put(3)
# 判断队列是否满了
print("当前队列是否已满：", q.full())
try:
    q.put(4, block=True, timeout=3)
except:
    print("队列已满，当前队列的深度为：%s" % q.qsize())
print("--------华丽的分割线--------")

print(q.get())
print(q.get())
print("当前队列是否已空：%s" % q.empty())
print(q.get())
# 判断队列是否为空
print("当前队列是否已空：%s" % q.empty())
try:
    q.get(block=True, timeout=3)
except:
    print("队列已空，当前队列的深度为：%s" % q.qsize())
print("--------华丽的分割线--------")


if __name__ == "__main__":
    pass
