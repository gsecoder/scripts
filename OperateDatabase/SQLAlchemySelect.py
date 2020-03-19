#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemySelect.py
@Time    :   2019/11/5 19:06
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   查询数据
"""
from OperateDatabase.SQLAlchemyConnect import News
from OperateDatabase.SQLAlchemyConnect import connect_database
from sqlalchemy.orm import sessionmaker


class SelectData(object):
    def __init__(self):
        Session = sessionmaker(bind=connect_database().engine)
        self.session = Session()

    def get_one(self):
        """查询一条数据"""
        return self.session.query(News).all()

    def get_more(self):
        """查询多条数据"""
        return self.session.query(News).filter(News.id > 9)

    def order_result(self):
        """查询结果排序"""
        return self.session.query(News).order_by(News.id)


if __name__ == "__main__":
    sd = SelectData()
    sd.get_one()
    # sd.get_more()
    # print(sd.order_result())

