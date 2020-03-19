#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemyConnect.py
@Time    :   2019/11/4 20:16
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   1.from SQLAlchemyConnect import News, engine
             2.News.metadata.create_all(engine)
             注意： sqlchemy对于Python3不友好， 链接数据库时需要用mysql+pymysql
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine
# 基类
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def connect_database():
    engine = create_engine(
        'mysql+pymysql://用户名:密码@XXX.XXX.XXX.125/PythonDatabases?charset=utf8',
        max_overflow=5,
        encoding='utf8'
    )
    Base.metadata.create_all(engine)
    return engine


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), )
    author = Column(String(20), )
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)
    # 添加配置设置编码
    __table_args__ = {
        'mysql_charset': 'utf8'
    }


if __name__ == "__main__":
    ns = News()

