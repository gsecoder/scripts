#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   204_stack.py
@Time    :   2019/10/23 21:20
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""栈"""
class Stack(object):
    def __init__(self):
        self.items = []

    """判断栈是否为空"""
    def is_empty(self):
        return self.items == []

    """加入元素"""
    def push_item(self, item):
        self.items.append(item)

    """弹出元素（删除元素）"""
    def pop_item(self):
        self.items.pop()

    """返回栈顶元素"""
    def peek_item(self):
        return self.items[len(self.items)-1]

    def size_item(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push_item("123")
    s.push_item("456")
    s.push_item("789")
    s.push_item("234")
    s.push_item("567")
    print(s.size_item())
    s.pop_item()
    print(s.peek_item())

