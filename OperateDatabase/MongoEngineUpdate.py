#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MongoEngineUpdate.py
@Time    :   2019/11/29 12:59
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.MongoEngineConnect import MongoConnect
from OperateDatabase.MongoEngineConnect import User


class UpdateData(object):
    def __init__(self):
        self.my_connect = MongoConnect()

    def update_data(self):
        print("成功建立mongodb连接: %s" % self.my_connect.DEFAULT_CONNECTION_NAME)
        user = User.objects.all()
        user = User.objects(name="9999xcv222333444")
        user.name = "dj"
        user.update()
        print(user.name)
        print("成功关闭连接: %s" % self.my_connect.close_connect())


if __name__ == "__main__":
    ud = UpdateData()
    ud.update_data()
