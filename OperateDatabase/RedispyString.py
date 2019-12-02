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
        self.rc.set(key, value)

     def mset_value(self):
         pass


if __name__ == "__main__":
    rs = RedisString()

    # 插入数据
    rs.set_value(key="RedispyString", value="set_value")