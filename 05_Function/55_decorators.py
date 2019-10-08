#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   55_decorators.py
@Time    :   2019/10/8 16:07
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

def auth():
    def authority(username, password):
        if username == 'crisimple' and password == '159357':
            print('欢迎回来，我的小主人...')
        else:
            print('登录失败...')

    return authority()

@auth
def view_space():
    user = input("请输入用户名：")
    passwd = input("请输入用户密码：")
    print("......认证成功，成功进入哔哩哔哩个人空间......")


view_space()

