#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   71_producer_consumer_model.py
@Time    :   2019/10/11 20:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import time
from multiprocessing import Process, JoinableQueue


def producer(qq, name):
    for i in range(3):
        res = "包子%s" % i
        time.sleep(0.5)
        print("%s 生产了 %s" % (name, res))
        qq.put(res)

def consumer(qq, name):
    while True:
        res = qq.get()
        if res is None:
            break
        time.sleep(1)
        print("%s 吃了%s" % (name, res))


def producer_j(qj, name):
    for i in range(3):
        res = "包子%s" % i
        time.sleep(0.5)
        print("%s 生产了 %s" % (name, res))
        qj.put(res)
    qj.join()

def consumer_j(qj, name):
    while True:
        res = qj.get()
        if res is None:
            break
        time.sleep(1)
        print("%s 吃了%s" % (name, res))
        qj.task_done()


if __name__ == "__main__":
    # 队列容器
    # qq = Queue()
    # # 生产者们
    # p1 = Process(target=producer, args=(qq, '生产者1'))
    # p2 = Process(target=producer, args=(qq, '生产者2'))
    # p3 = Process(target=producer, args=(qq, '生产者3'))
    # # 消费者们q
    # c1 = Process(target=consumer, args=(qq, '消费者1'))
    # c2 = Process(target=consumer, args=(qq, '消费者2'))
    # p1.start()
    # p2.start()
    # p3.start()
    # c1.start()
    # c2.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # qq.put(None)
    # qq.put(None)
    # print("主进程")

    # ------------------------
    qj = JoinableQueue()
    # 生产者们
    pj1 = Process(target=producer_j, args=(qj, "生产者j1"))
    pj2 = Process(target=producer_j, args=(qj, "生产者j2"))
    pj3 = Process(target=producer_j, args=(qj, "生产者j3"))
    # 消费者们
    cj1 = Process(target=consumer_j, args=(qj, "消费者j1"))
    cj2 = Process(target=consumer_j, args=(qj, "消费者j2"))
    cj1.daemon = True  # 若不添加守护进程，则会卡在消费者
    cj2.daemon = True

    pj1.start()
    pj2.start()
    pj3.start()
    cj1.start()
    cj2.start()
    pj1.join()
    pj2.join()
    pj3.join()
    print('JoinableQueue主进程')

