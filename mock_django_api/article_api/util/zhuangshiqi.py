#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : zhuangshiqi.py 
__author__ : crisimple
__date__   : 2020-05-26 11:25
__function__:
装饰器小回顾
"""

def user_auth(func):
    def auth():
        print("这是装饰器函数要实现的功能，可以搞一些逻辑判断的条件")

        # 这个func值的是要被装饰器的函数
        func()

    return auth

@user_auth
def my_wallet():
    print("钱包余额：99999999999")


if __name__ == "__main__":
    my_wallet()
