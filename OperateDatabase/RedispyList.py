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
        @param k: key
        @param v: value
        @return:
        """
        return self.rc.lpush(k, v)

    def rpush_data(self, k=None, v=None):
        """
        从右边插入数据
        @param k: key
        @param v: value
        @return:
        """
        return self.rc.rpush(k, v)

    def lrange_get(self, k=None, s=None, e=None):
        """
        获取列表的数据
        @param k: key
        @param s: 起始位置
        @param e: 结束位置
        @return: 返回列表数据
        """
        return self.rc.lrange(k, s, e)

    def ltrim_get(self, k=None, s=None, e=None):
        """
        截取列表
        @param k: key
        @param s: 截取的开始位置
        @param e: 截取的结束位置
        @return:
        """
        print("原列表：%s" % self.rc.lrange(k, 0, -1))
        print("截取列表：%s" % self.rc.ltrim(k, s, e))
        print("截取后的列表：%s", self.rc.lrange(k, 0, -1))

    def lpop_data(self, k):
        """
        从列表的最左边移除一个元素
        @param k: key
        @return: 返回移除的元素
        """
        return self.rc.lpop(k)

    def rpop_data(self, k):
        """
         从列表的最右边移除一个元素
        @param k: key
        @return: 返回移除的元素
        """
        return self.rc.rpop(k)

    def lpushx_data(self, k, v):
        """
        k存在的时候从左边插入v，k不存在的时候不做任何处理
        @param k: key
        @param v: val
        @return: 返回处理后列表的长度
        """
        return self.rc.lpushx(k, v)

    def rpushx_data(self, k, v):
        """
        k存在的时候从右边插入v，k不存在的时候不做任何处理
        @param k: key
        @param v: val
        @return: 返回处理后列表的长度
        """
        return self.rc.rpushx(k, v)


if __name__ == "__main__":
    rl = RedisLists()
    # print(rl.rc)

    # 从左边插入数据
    # print(rl.lpush_data("list1", "v11"))
    # print(rl.lpush_data(k="list1", v="v12"))
    # print(rl.lpush_data(k="list1", v="v13"))
    # print(rl.lrange_get(k="list1", s=0, e=-1))

    # 从右边插入数据
    # print(rl.rpush_data(k="list1", v="v21"))
    # print(rl.rpush_data(k="list1", v="v22"))
    # print(rl.rpush_data(k="list1", v="v23"))
    # print(rl.lrange_get(k="list1", s=0, e=-1))

    # 截取数据
    # rl.ltrim_get(k="list1", s=0, e=3)

    # 从最左边移除元素
    # print(rl.lrange_get(k="list1", s=0, e=-1))
    # print(rl.lpop_data(k="list1"))
    # print(rl.lrange_get(k="list1", s=0, e=-1))

    # 从最右边移除元素
    # print(rl.lrange_get(k="list1", s=0, e=-1))
    # print(rl.lpop_data(k="list1"))
    # print(rl.lrange_get(k="list1", s=0, e=-1))

    # 不存在的key
    # print(rl.lrange_get(k="list2", s=0, e=-1))
    # print(rl.lpushx_data(k="list2", v="test_list2"))
    # 存在的key
    # print(rl.lrange_get(k="list1", s=0, e=-1))
    # print(rl.lpushx_data(k="list1", v="test_list1"))

