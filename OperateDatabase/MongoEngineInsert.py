#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MongoEngineInsert.py
@Time    :   2019/11/27 20:55
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime
from OperateDatabase.MongoEngineConnect import MongoConnect


class Categories(Document):
    """
    定义分类文档
    继承Document类,为普通文档
    Categories对应到mongodb数据库就是一个集合categories
    """
    name = StringField(max_length=30, required=True)
    artnum = IntField(default=0, required=True)
    date = DateTimeField(default=datetime.now(), required=True)

# 插入数据类
class InsertData(object):
    def __init__(self):
        self.my_connect = MongoConnect()
        print("成功建立mongodb连接: %s" % self.my_connect.DEFAULT_CONNECTION_NAME)

    def insert_data(self):
        Categories(name="J").save()
        print("成功关闭mongodb连接: %s" % self.my_connect.close_connect())

    def insert_datas(self):
        for i in range(5, 10):
            Categories(name="%s" % i).save()
        print("成功关闭mongodb连接: %s" % self.my_connect.close_connect())


if __name__ == "__main__":
    ids = InsertData()
    # 插入一条数据
    # ids.insert_data()
    # 插入多条数据
    ids.insert_datas()
