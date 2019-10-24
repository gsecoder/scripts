#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2051_queue.py
@Time    :   2019/10/23 21:43
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""队列"""
class Queue(object):
    def __init__(self):
        self.items = []

    """判断队列是否为空"""
    def is_empty(self):
        return self.items == []

    # 【["队尾", ..., "对头"]】
    """进队列：只允许在队尾插入数据"""
    def enqueue(self, item):
        self.items.insert(0, item)

    """出队列：只允许在对头删除"""
    def dequeue(self):
        return self.items.pop()

    """返回队列的大小"""
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue("123")
    q.enqueue("456")
    q.enqueue("789")
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())

