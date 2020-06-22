#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   message_models.py
@Time    :   2020/4/1320:23
@Author  :   jiangheng
@Description    :   None
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)
# 配置数据库
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "message_board.db"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:Root@159357@129.28.170.125:3306/message_board'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECERT_KEY"] = "test_password"
app.secret_key = "qwert"

# 实例化数据库
db = SQLAlchemy(app)

# 管理员表
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)    # 主键
    username = db.Column(db.String(32), nullable=False, unique=True)     # 账号
    password = db.Column(db.String(64), nullable=False)     # 密码
    tags = db.relationship("Tag", backref="admin")      # 标签

# 标签表
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)    # 主键
    name = db.Column(db.String(10), nullable=False, unique=True)     # 标签名
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))     # 所属管理员

# 用户表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)    # 主键
    username = db.Column(db.String(32), nullable=False, unique=True)     # 账号
    password = db.Column(db.String(64), nullable=False)     # 密码
    messages = db.relationship("Message", backref="user")      # 标签

# 留言表
class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)    # 主键
    content = db.Column(db.String(256), nullable=False)     # 内容
    create_time = db.Column(db.DateTime, default=datetime.now)      # 发布留言时间
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))     # 所属用户
    tags = db.relationship("Tag", secondary="message_to_tag", backref="messages")   # 关系关联

# 中间表
class MessageToTag(db.Model):
    __tablename__ = "message_to_tag"
    id = db.Column(db.Integer, primary_key=True)    # 主键
    message_id = db.Column(db.Integer, db.ForeignKey("message.id"))     # 所属留言
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))     # 所属标签


if __name__ == "__main__":
    db.create_all()
    # db.drop_all()
