#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MongoEngineSelect.py
@Time    :   2019/11/28 21:23
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.MongoEngineConnect import MongoConnect, User

class SelectData(object):
    def __init__(self):
        self.my_connect = MongoConnect()

    def select_data(self):
        print("成功建立mongodb连接: %s" % self.my_connect.DEFAULT_CONNECTION_NAME)
        for i in User.objects.all():
            print("返回文档对象的列表: %s" % i)
            print("返回所有符合查询条件的结果的文档对象列表: %s" % i.name)
        print("成功关闭mongodb连接: %s" % self.my_connect.close_connect())

    # def update_select_data(self):
    #     """
    #     更新查询
    #     :return:
    #     """
    #     print("成功建立mongodb连接: %s" % self.my_connect.DEFAULT_CONNECTION_NAME)
    #     user = User(name="9999xcv")
    #     user.name = "9999xcv222333444"
    #     user.save()
    #
    #     print(user.objects)


if __name__ == "__main__":
    # SelectData().select_data()

    SelectData().update_select_data()