#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2032_sincycLinkedList.py
@Time    :   2019/10/23 20:53
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedList(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None

    """判断链表是否为空"""
    def is_empty(self):
        return self._head is None

    """返回链表的长度"""
    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next is not self._head:
            count += 1
            cur = cur.next
        return count

    """遍历链表"""
    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)
        while cur.item != self._head:
            cur = cur.next
            print(cur.item)
        print(" ")

    """添加节点"""
    def add_item(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 添加的节点时间指向_head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            #_head指向添加node的
            self._head = node

    def append_item(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head

    def insert_item(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove_item(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next

    def search_item(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    scll = SinCycLinkedList()
    print(scll.is_empty())
    print(scll.length())
