#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   net_ease.py
@Time    :   2019/11/6 14:27
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :
        1. 在python shell中创建数据表饿数据库
            from net_ease import db
            db.create_all()
        2. 创建一些表的实例，也就是插入一些数据
            from net_ease import News
            news1 = News(title='title1', content="content1", types="type1")
            news2 = News(title='title2', content="content2", types="type2")
            news3 = News(title='title3', content="content3", types="type3")
            db.session.add(news1)
            db.session.add(news2)
            db.session.add(news3)
            db.session.commit()
        3. 查询数据库中的数据

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Boolean

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Root@159357@129.28.170.125:3306/NetEase?charset=utf8'
db = SQLAlchemy(app)


# 创建应用的数据表
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300))
    author = db.Column(db.String(200))
    view_count = db.Column(db.Integer)
    create_at = db.Column(DateTime)
    is_valid = db.Column(Boolean)

    def __init__(self, title, content, types):
        self.title = title
        self.content = content
        self.types = types

    def __repr__(self):
        return '<News %r>' % self.id


