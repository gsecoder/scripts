#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PymongoDelete.py
@Time    :   2019/11/27 15:26
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PymongoConnect import PymongoOperate


class DeleteData(object):

    def __init__(self, db_para=None, collection_para=None):
        self.po = PymongoOperate()
        # 建立数据库连接
        self.my_client = self.po.client
        # 使用数据库
        self.my_db = self.my_client[db_para]
        # 使用集合
        self.my_collection = self.my_db[collection_para]

    def delete_data(self, del_data=None):
        """
        删除单条数据
        :param del_data:
        :return: {'n': 1, 'ok': 1.0} -- n为1，代表删除的数据存在
                 {'n': 1, 'ok': 1.0} -- n为1，代表删除的数据不存在
        """
        res = self.my_collection.delete_one(del_data)
        return res.raw_result

    def delete_datas(self, del_data=None):
        res = self.my_collection.delete_many(del_data)
        return res.deleted_count
        # return res.raw_result

    def delete_all(self, del_data=None):
        res = self.my_collection.delete_many({})
        return res.deleted_count

    def delete_collection(self):
        res = self.my_collection.drop()
        return res

if __name__ == "__main__":
    dd = DeleteData(db_para="PyData", collection_para="id_apps")

    # 删除集合一条数据
    # print(dd.delete_data(del_data={"_id": 3}))

    # 删除集合多条数据
    # print(dd.delete_datas(del_data={"name": {"$regex": "^G"}}))

    # 删除集合所有数据
    # print(dd.delete_all())

    # 删除集合
    # print(dd.delete_collection())