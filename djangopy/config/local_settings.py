#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : local_settings.py
__time__    : 2020/6/25 16:52
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

""" django显示语言 """
LANGUAGE_CODE = 'zh-hans'

""" 腾讯短信关键配置信息 """
TENCENT_SMS_APP_ID = "1400367199"
TENCENT_SMS_APP_KEY = "43d2c318088e57f4141f5b190da0f577"
TENCENT_SMS_SIGN = "DeepHub"
TENCENT_SMS_TEMPLATE = {
    "register": 646235,
    "login": 646236
}

""" Django-Redis 配置信息 """
CACHES = {
    "default": {
        "BACKED": "django-redis.cache.RedisCache",
        "LOCATION": "redis://129.28.170.125:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django-redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS":{
                "max_connections": 1000,
                "encoding": "utf-8"
            },
            "PASSWORD": "159357"
        }
    },
    "default2": {
        "BACKED": "django-redis.cache.RedisCache",
        "LOCATION": "redis://129.28.170.125:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django-redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS":{
                "max_connections": 1000,
                "encoding": "utf-8"
            },
            "PASSWORD": "159357"
        }
    }
}
