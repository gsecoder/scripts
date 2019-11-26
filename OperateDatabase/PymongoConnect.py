#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PymongoConnect.py
@Time    :   2019/11/25下午11:05
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from pymongo import MongoClient


class PymongoOperate(object):
    """
    连接mongodb数据库
    """
    def __init__(self):
        self.client = MongoClient(
            host="xxx.xxx.xxx.xxx",
            port=27017,
            username="用户名",
            password="用户密码"
        )

    """
    创建mongodb数据库
    创建集合collection
    """
    def create_db_collection(self):
        # 查询当前数据库中存在那些mongodb数据库
        # global my_db
        db_lists = self.client.list_database_names()
        print("存在数据库有：%s" % db_lists)
        # 如果数据库不存在与当前数据库列表中创建数据库，否则提示-数据库已存在
        new_mongodb = "PyData"
        if new_mongodb in db_lists:
            print("%s 已存在于 %s 中了" % (new_mongodb, db_lists))
        my_db = self.client[new_mongodb]
        new_db_lists = self.client.list_database_names()
        print("创建新数据库后，存在的数据库有：%s" % new_db_lists)

        # 查询当前数据库中的集合
        collection_lists = my_db.list_collection_names()
        print("已存在的集合有： %s" % collection_lists)
        # 如果数据库不存在集合则创建集合，否则提示-集合已存在
        new_collection = "py_collection"
        if new_collection in collection_lists:
            print("%s 存在于 %s" % (new_collection, collection_lists))
        my_collection = my_db[new_collection]
        new_collection_lists = my_db.list_collection_names()
        print("创建新集合后，存在的集合有：%s" % new_collection_lists)

    def close_connect(self):
        try:
            if self.client:
                return self.client.close()
        except Exception as e:
            print("Error: %s" % e)


if __name__ == "__main__":
    po = PymongoOperate()
    po.create_db_collection()
