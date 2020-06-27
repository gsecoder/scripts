#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : operate_redis.py
__time__    : 2020/6/26 18:38
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import redis

"""
    直接连接redis
    创建 redis 连接池
    默认最大连接数为：2**31 个
"""
pool = redis.ConnectionPool(
    host="129.28.170.125",
    port=6379,
    password=159357,
    encoding="utf-8",
    max_connections=1000
)

""" 去连接池中取一个连接 """
conn = redis.Redis(connection_pool=pool)

# 设置键值：15131255089="9999"，且超时时间为 10 秒（值写到 redis 时会自动转为字符串）
conn.set('15131255089', 9999, ex=10)

# 根据键值获取值
value = conn.get("15131255089")

print(value)