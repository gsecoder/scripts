#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2052_deque.py
@Time    :   2019/10/24 12:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""双端队列"""
class Deque(object):
    def __init__(self):
        self.items = []

    """判断双端队列是否为空"""
    def is_empty(self):
        self.items == []

    """在队头添加元素"""
    def add_front(self, item):
        self.items.insert(0, item)

    """在队尾添加元素"""
    def add_rear(self, item):
        self.items.append(item)

    """在对头移除元素"""
    def remove_front(self):
        return self.items.pop(0)

    """在队尾移除元素"""
    def remove_rear(self):
        return self.items.pop()

    """返回双端队列的大小"""
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    d = Deque()
    d.add_front(1)
    d.add_front(2)
    d.add_rear(3)
    d.add_rear(4)
    print(d.size())
    print(d.remove_front())
    print(d.remove_front())
    print(d.remove_rear())
    print(d.remove_rear())
    print(d.size())
