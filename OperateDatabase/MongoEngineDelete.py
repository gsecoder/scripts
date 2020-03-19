#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MongoEngineDelete.py
@Time    :   2019/11/29 12:57
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import mongoengine
from OperateDatabase.MongoEngineConnect import MongoConnect


class DeleteData(object):
    def __init__(self):
        self.my_connect = MongoConnect()

    def delete_data(self):
        print("成功建立mongodb连接: %s" % self.my_connect.DEFAULT_CONNECTION_NAME)
        user1 = mongoengine.ReferenceField(name="User", reversed_delete_rule=mongoengine.CASCADE)
        print(user1)


if __name__ == "__main__":
    dd = DeleteData()
    dd.delete_data()