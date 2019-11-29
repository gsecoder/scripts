#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MongoEngineConnect.py
@Time    :   2019/11/27 20:28
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from mongoengine import connect, disconnect
from mongoengine import Document, StringField, IntField, DateTimeField
import datetime


class MongoConnect(object):

    def __init__(self):
        """
         db=None,
         alias=None,
         host=None,
         port=None,
         username=None,
         password=None,
         authentication_source=None
        """
        self.DEFAULT_CONNECTION_NAME = connect(
            # 需要连接数据库
            db="PyData",
            # 对连接的mongodb数据库起个别名，方便连接多个数据库【这是个坑】
            # alias="Al_PyData",
            # mongodb数据库服务器ip
            host="xxx.xxx.xxx.xxx",
            # mongodb数据库的端口号
            port=27017,
            # 用户名字
            username="用户名",
            # 用户密码
            password="用户密码",
            # 进行身份认证的数据库，一般都是admin
            authentication_source="admin"
        )

    def close_connect(self):
        try:
            if self.DEFAULT_CONNECTION_NAME:
                return disconnect()
        except Exception as e:
            print("Error: %s" % e)


# 定义一个文档User类，继承与Document
class User(Document):
    name = StringField(max_length=30, required=True)
    types = IntField(default=0, required=True)
    date = DateTimeField(default=datetime.datetime.now(), required=True)


if __name__ == "__main__":
    mc = MongoConnect()
    print("连接成功返回：%s" % mc.DEFAULT_CONNECTION_NAME)
    for i in range(10):
        User(name="%s" % i).save()
    print("成功关闭mongodb连接: %s" % disconnect())
