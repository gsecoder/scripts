#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemyInsert.py
@Time    :   2019/11/5 10:19
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.SQLAlchemyConnect import connect_database
from sqlalchemy.orm import sessionmaker
from OperateDatabase.SQLAlchemyConnect import News


class InsertData(object):
    def __init__(self):
        Session = sessionmaker(bind=connect_database().engine)
        self.session = Session()

    def add_one(self):
        news1 = News(
            title="new1",
            content="new1content1",
            types="baijia"
        )
        news2 = News(
            title="new2",
            content="new1content2",
            types="baijia2"
        )
        news3 = News(
            title="新闻3",
            content="新闻3的Content",
            types="百家3"
        )
        news = [
            News(title="news3", content="news3Content", types="baijia3"),
            News(title="news4", content="news4Content", types="baijia4"),
            News(title="news5", content="news5Content", types="baijia5")
        ]
        # 插入单条数据
        # self.session.add(news1)
        # self.session.add(news2)
        # self.session.add(news)

        # 插入多条数据
        self.session.add_all(news)
        self.session.commit()
        return news

if __name__ == "__main__":
    id1 = InsertData()
    print(id1.add_one())

