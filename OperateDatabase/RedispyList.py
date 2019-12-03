#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RedispyList.py
@Time    :   2019/12/314:25
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.RedispyConnect import RedisConnect


class RedisLists(object):

    def __init__(self):
        self.rc = RedisConnect().redis_connect

    def lpush_data(self, k=None, v=None):
        """
        从左边插入数据
        @param k:
        @param v:
        @return:
        """
        return self.rc.lpush(k, v)

    def rpush_data(self, k=None, v=None):
        """
        从右边插入数据
        @param k:
        @param v:
        @return:
        """
        return self.rc.rpush(k, v)

    def lrange_get(self, start=None, end=None):
        """
        获取列表的数据
        @param start:
        @param end:
        @return:
        """
        return self.rc.lrange(start, end)


if __name__ == "__main__":
    rl = RedisLists()
    # print(rl.rc)

    # 从左边插入数据
    rl.lpush_data("list1", "v11")
    # print(rl.lpush_data(k="list1", v="v12"))
    # print(rl.lpush_data(k="list1", v="v13"))
    # print(rl.lrange_get(0, -1))

    # 从右边插入数据
    # print(rl.rpush_data(k="list1", v="v21"))
    # print(rl.rpush_data(k="list1", v="v22"))
    # print(rl.rpush_data(k="list1", v="v23"))
    # print(rl.lrange_get(0, -1))
