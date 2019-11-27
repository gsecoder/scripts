#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PymongoSelect.py
@Time    :   2019/11/27 17:46
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PymongoConnect import PymongoOperate

class SelectData(object):

    def __init__(self, db_para=None, collection_para=None):
        po = PymongoOperate()
        my_client = po.client
        self.my_db = my_client[db_para]
        self.my_collection = self.my_db[collection_para]

    def select_one(self):
        res = self.my_collection.find_one()
        print("查询一条数据的结果为：%s" % res)

    def select_all(self):
        res = self.my_collection.find()
        for i in res:
            print("查询集合中所有的结果为：%s" % i)

    def select_col(self, col_val=None):
        """
        查询指定字段
        :param col_val: 指定的字段
        :return:
        """
        res = self.my_collection.find({}, col_val)
        print("查询指定字段的数据：")
        for i in res:
            print("%s" % i)

    def select_condition(self, condition=None):
        """
        指定条件的查询
        :param condition: 查询条件
        :return:
        """
        res = self.my_collection.find(condition)
        print("指定条件的查询结果为：")
        for i in res:
            print(i)

    def select_sort(self, col=None, ids=None):
        """
        查询排序
        :param col: 要排序的列
        :param ids: 1：升序（默认）；-1：降序
        :return:
        """
        res = self.my_collection.find().sort(col, ids)
        print("排序结果为：")
        for i in res:
            print(i)


if __name__ == "__main__":
    sd = SelectData(db_para="PyData", collection_para="apps")

    # 查询一条数据
    # sd.select_one()

    # 查询所有数据
    # sd.select_all()

    # 查询指定字段的数据
    col_val_1 = {"_id": 0, "name": 1, "url": 1}
    # sd.select_col(col_val=col_val_1)

    # 指定条件的查询
    condition_1 = {"name": "Github"}
    # sd.select_condition(condition=condition_1)

    # 查询后排序
    col_1 = "alexa"
    ids_1 = -1
    sd.select_sort(col=col_1, ids=ids_1)


