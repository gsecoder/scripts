#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemyCombat.py
@Time    :   2019/11/4 20:16
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from sqlalchemy import create_engine
# 基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine("mysql://root:Root@159357@129.28.170.125/PythonDatabases")
Base = declarative_base()


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
