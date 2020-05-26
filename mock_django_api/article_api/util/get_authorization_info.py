#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : get_authorization_info.py
__author__ : jiangheng
__date__   : 2020-05-26 9:15
__function__:
    authorization -- 用户认证（参考博客：https://www.cnblogs.com/linxiyue/p/4079768.html）
    这里解码的是 Basic Authorization 信息，可参考 postman 的 Basic Auth 用户认证
"""
import base64

import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)

""" 解码Basic Auth中的用户名密码 """
def decode_user_password(str1):
    decode_base = str1.replace('Basic ', '')
    # print("decode_base: ", decode_base)
    decode_info = base64.b64decode(decode_base)
    # print("type of decode_info: ", type(decode_info))
    str_decode_info = str(decode_info)
    # print("type of str_decode_info: ", type(str_decode_info))
    # print("str_decode_info: ", str_decode_info)
    user_info = str_decode_info[2:-1].split(':')
    return user_info

""" 通过"""
def encode_user_password(str_user, str_password):
    str_join = str_user + ":" + str_password
    print("str_join: ", str_join)


if __name__ == "__main__":
    str_info = 'Basic Y3Jpc2ltcGxlOjE1OTM1Nw=='
    print(decode_user_password(str_info))
    # encode_user_password('s1', '132')