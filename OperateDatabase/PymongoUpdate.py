#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PymongoUpdate.py
@Time    :   2019/11/27 17:25
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PymongoConnect import PymongoOperate


class UpdateData(object):

    def __init__(self, db_para=None, collection_para=None):
        self.po = PymongoOperate()
        self.my_client = self.po.client
        self.my_db = self.my_client[db_para]
        self.my_collection = self.my_db[collection_para]

    def update_data(self, old_val=None, new_val=None):
        res = self.my_collection.update_one(old_val, new_val)
        # return res.matched_count
        for i in self.my_collection.find():
            print(i)

    def update_datas(self, old_val=None, new_val=None):
        res = self.my_collection.update_many(old_val, new_val)
        for i in self.my_collection.find():
            print(i)


if __name__ == "__main__":
    ud = UpdateData(db_para="PyData", collection_para="apps")

    # 更新集合中的一条数据
    old_val_1 = {"company": "xiaomi"}
    new_val_1 = {"$set": {"company": "xiaomi_update"}}
    # ud.update_data(old_val=old_val_1, new_val=new_val_1)

    # 更新集合中的多条数据
    old_val_2 = {"name": {"$regex": "^Zha"}}
    new_val_2 = {"$set": {"name": "ZhaZha********"}}
    ud.update_datas(old_val=old_val_2, new_val=new_val_2)
