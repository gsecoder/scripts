#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   71_Process_mutextlock.py
@Time    :   2019/10/11 16:40
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
from multiprocessing import Process, Lock
import time
import json

# 未加互斥锁
def unlock(name):
    print("%s 1" % name)
    time.sleep(1)
    print("%s 2" % name)
    time.sleep(1)
    print("%s 3" % name)

# ------------------------------------------------------------
# 加互斥锁
def lock(name, mutex):
    mutex.acquire()
    print('%s 1' % name)
    time.sleep(1)
    print('%s 2' % name)
    time.sleep(1)
    print('%s 3' % name)
    mutex.release()

# ------------------------------------------------------------
# 模拟抢票过程
def search_ticket(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    print("<%s> 查看到剩余票数为【%s】" % (name, dic['count']))

def buy_ticket(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(3)
        json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
        print('<%s> 购票成功' % name)
    else:
        print('<%s> 暂无余票' % name)

def ticket_task(name, mutex):
    # 查票每个人都可以执行，是并发执行操作
    search_ticket(name)
    mutex.acquire()     # 添加互斥锁，达到串行执行，使得只有一个人购票成功
    buy_ticket(name)
    mutex.release()


if __name__ == "__main__":
    # for i in range(3):
    #     p_unlock = Process(target=unlock, args=("未进程%s" % i,))
    #     p_unlock.start()
    # 执行结果：
    # ------------------------
    # 进程0 1
    # 进程1 1
    # 进程2 1
    # 进程0 2
    # 进程1 2
    # 进程2 2
    # 进程0 3
    # 进程1 3
    # 进程2 3

    # mutex = Lock()
    # for i in range(3):
    #     p_lock = Process(target=lock, args=("加锁进程%s" % i, mutex))
    #     p_lock.start()
    # 执行结果：
    # ------------------------
    # 加锁进程0 1
    # 加锁进程0 2
    # 加锁进程0 3
    # 加锁进程1 1
    # 加锁进程1 2
    # 加锁进程1 3
    # 加锁进程2 1
    # 加锁进程2 2
    # 加锁进程2 3

    # 模拟抢票
    mutex = Lock()
    for i in range(10):
        p_ticket = Process(target=ticket_task, args=("乘客%s" % i, mutex))
        p_ticket.start()
        # 利用互斥锁，可以通过添加互斥锁的位置，实现部分程序执行达到串行的效果，其他程序仍然可以并行执行，而添加了join只能执行完了之后才能执行下一个，若作为每项都添加一个join，则都要串行执行。从而大大降低了效率。
        p_ticket.join()


