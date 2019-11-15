#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemyUpdate.py
@Time    :   2019/11/5 20:59
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.SQLAlchemyConnect import connect_database
from sqlalchemy.orm import sessionmaker
from OperateDatabase.SQLAlchemyConnect import News


class UpdateData(object):
    def __init__(self):
        Session = sessionmaker(bind=connect_database().engine)
        self.session = Session()

    def update_data(self, pk):
        """修改数据"""
        data_lists = self.session.query(News).filter_by(id=7)
        for item in data_lists:
            item.title = "XXX"
            self.session.add(item)
        self.session.commit()


if __name__ == "__main__":
    ud = UpdateData()
    ud.update_data(7)

