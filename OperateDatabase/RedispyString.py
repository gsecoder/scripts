#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RedispyString.py
@Time    :   2019/12/2下午10:13
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.RedispyConnect import RedisConnect

class RedisString(object):

    def __init__(self):
        self.rc = RedisConnect().redis_connect

    def set_value(self, key=None, value=None):
        """
        插入单条数据
        """
        return self.rc.set(key=key, value=value)

    def get_value(self, k=None):
        """
        获取单条数据
        @param k: key值
        @return:
        """
        return self.rc.get(k)

    def mset_values(self, **kwargs):
        """
        插入多条数据
        @param kwargs:
        @return:
        """
        return self.rc.mset(kwargs)

    def mget_values(self, *args):
        """
        获取多条数据
        @param args:
        @return:
        """
        return self.rc.mget(args)

    def append_value(self, k=None, av=None):
        """
        给k对应的value追加值
        @param k: key
        @param av: append_value
        @return: 添加后的value的总长度
        """
        return self.rc.append(k, av)
        print(self.rc.append(k, av))

    def del_key(self, k=None):
        """
        删除key和对应的值
        @param k:
        @return:
        """
        return self.rc.delete(k)

    def incr_data(self, k=None, v=None):
        """
        自增加1
        @param k:
        @param v:
        @return:
        """
        print(self.rc.set(k, v))
        print(self.rc.get(k))
        print(self.rc.incr(k))
        print(self.rc.get(k))

    def decr_data(self, k=None, v=None):
        """
        自减少1
        @param k:
        @param v:
        @return:
        """
        print(self.rc.set(k, v))
        print(self.rc.get(k))
        print(self.rc.decr(k))
        print(self.rc.get(k))


if __name__ == "__main__":
    rs = RedisString()
    print(rs.rc)

    # 插入单条数据
    # rs.set_value(key="RedispyString", value="set_value2")
    # 获取单条数据
    # print(rs.get_value(k='RedispyString'))

    # 插入多条数据
    # rs.mset_values(RedispyStringK1="v1", RedispyStringK2="v2")
    # 获取多条数据
    # print(rs.mget_values('RedispyStringK1', 'RedispyStringK2'))

    # 给k对应的value追加值
    # rs.append_value(k="RedispyStringK1", av="_appendValue")
    # rs.append_value(k="RedispyStringK_None", av="_appendValue")

    # 删除数据
    # print(rs.del_key(k="RedispyStringK_None"))

    # 自增加1
    # rs.incr_data(k="RedispyStringIncrNum", v=10)

    # 自减少1
    # rs.decr_data(k="RedispyStringDecrNum", v=20)
