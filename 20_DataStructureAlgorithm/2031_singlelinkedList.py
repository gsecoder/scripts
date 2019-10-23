#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2031_singlelinkedList.py
@Time    :   2019/10/23 17:13
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 节点的实现
class SingleNode(object):
    """单链表的节点"""
    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        # next 是下一个节点的标识
        self.next = None


# 单链表的实现
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        # 尾节点指向None，当为到达尾部时
        while cur is not None:
            count = count + 1
            # cur向后移动一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print(" ")

    def add_item(self, item):
        """头部添加元素"""
        # 创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append_item(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert_item(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add_item(item)
        elif pos > (self.length() - 1):
            self.append_item(item)
        # 指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove_item(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                # 如果第一个就是删除节点
                if not pre:
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的最后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search_item(self, item):
        """查找链接中元素是否存在"""
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    sll = SingleLinkList()
    sll.add_item(11)
    sll.add_item(12)
    sll.add_item(13)
    sll.travel()
    sll.insert_item(1, 14)
    sll.travel()
    print(sll.search_item(12))
