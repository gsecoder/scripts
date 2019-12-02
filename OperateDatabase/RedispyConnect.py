#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   
@Time    :   2019/12/219:02
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import redis

class RedisConnect(object):
    def __int__(self):
        self.r = redis.StrictRedis(
            host="xxx.xxx.xxx.xxx",
            port=6379,
            password="用户密码",
            db=0
        )

        return self.r


if __name__ == "__main__":
    print(RedisConnect().r)
    # print(rc.r)
