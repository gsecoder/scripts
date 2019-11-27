#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PymongoInsert.py
@Time    :   2019/11/26 10:05
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PymongoConnect import PymongoOperate

class InsertData(object):
    def __init__(self):
        self.po = PymongoOperate()
        self.my_client = self.po.client

    def insert_data(self, db_para, collect_para, data_para):
        """
        插入一条数据
        :param db_para: 被插入的数据库
        :param collect_para: 被插入的集合
        :param data_para: 要插入的数据
        :return: 返回插入后的对象
        """
        my_db = self.my_client[db_para]
        my_collection = my_db[collect_para]
        res = my_collection.insert_one(data_para)
        print(res.inserted_id)

    def insert_datas(self, db_paras2=None, collect_paras2=None, data_paras2=None):
        """
        插入多条数据
        :param db_paras2: 被插入的数据库
        :param collect_paras2:被插入的集合
        :param data_paras2: 要插入的多条数据
        :return:
        """
        my_db = self.my_client[db_paras2]
        my_collection = my_db["apps"]
        res = my_collection.insert_many(data_paras2)
        print(res.inserted_ids)

    def id_insert_datas(self, db_para=None, collect_para=None, data_para=None):
        """
        指定id插入多条数据
        :param db_para:
        :param collect_para:
        :param data_para:
        :return:
        """
        my_db = self.my_client[db_para]
        my_collection = my_db["id_apps"]
        res = my_collection.insert_many(data_para, ordered=False)
        print(res.inserted_ids)


if __name__ == "__main__":
    ind = InsertData()

    """插入一条数据"""
    db_para1 = "PyData"
    collect_para1 = "mobile"
    data_para1 = {
        "company": "xiaomi", "product": "xiaomi9", "price": 2599, "release_time": "2019"
    }
    # ind.insert_data(db_para=db_para1, collect_para=collect_para1,data_para=data_para1)

    """插入多条数据"""
    db_para2 = "PyData"
    # collect_para2 = "apps",
    data_para2 = [
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "Zhihu", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    # ind.insert_datas(db_paras2=db_para2, data_paras2=data_para2)

    """指定id插入多条数据"""
    db_para3 = "PyData"
    collect_para3 = "id_apps",
    data_para3 = [
        {"_id": 1, "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"_id": 2, "name": "Zhihu", "alexa": "103", "url": "https://www.zhihu.com"},
        {"_id": 3, "name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    ind.id_insert_datas(db_para=db_para3, data_para=data_para3)
