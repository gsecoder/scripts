#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   A
@Time    :   2019/12/219:02
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import redis


class RedisConnect(object):
    redis_connect = redis.Redis(
        host="129.28.170.125",
        port=6379,
        password="Root@159357",
        db=0
    )


if __name__ == "__main__":
    rc = RedisConnect.redis_connect
    # rc.__redis.set()
    print(rc.set())
    # print(rc.r)
