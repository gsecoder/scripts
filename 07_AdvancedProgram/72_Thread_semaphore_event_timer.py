#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   72_Thread_semaphore_event_timer.py
@Time    :   2019/10/14 19:55
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. 信号量（Semaphore）
from threading import Thread, Semaphore, currentThread

# 信号量大小，也就是同一时间3个任务去拿锁
sm = Semaphore(3)

def semaphore_task():
    sm.acquire()
    print("%s in" % currentThread().getName())
    sm.release()


# 2. Event
#  有多个工作线程尝试链接MySQL，我们想要在连接前确保MySQL服务正常才让那些工作线程去连接MySQL服务器，
#  如果连接不成功，都会去尝试重新连接。那么我们就可以采用threading.Event机制来协调各个工作线程的连接操作
from threading import Event, Thread, currentThread
import time

event = Event()

def conn_mysql():
    n = 0
    while not event.is_set():
        # print("event.is_set(): ", event.is_set())
        if n == 3:
            print("%s try many times" % currentThread().getName())
            return
        print("%s try %s" % (currentThread().getName(), n))
        event.wait(0.5)
        n += 1
    print("%s is connected" % currentThread().getName())

def check():
    print("%s is checking" % currentThread().getName())
    time.sleep(1)
    event.set()


# 3. 定时器（Timer）
from threading import Timer
def after_run():
    print("定时器指定时长后再执行程序")


if __name__ == "__main__":
    # 1.Semaphore
    # for i1 in range(10):
    #     t1 = Thread(target=semaphore_task)
    #     t1.start()

    # 2.Event
    # for i2 in range(3):
    #     t = Thread(target=conn_mysql)
    #     t.start()
    # t = Thread(target=check)
    # t.start()

    # 3. Timer
    t3 = Timer(2, after_run)
    t3.start()
