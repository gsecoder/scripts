#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : operate_database.py 
__author__ : crisimple
__date__   : 2020-06-01 16:56
__function__:
    操作 mysql 数据库
"""
import pymysql

class OperateDatabase(object):

    def __init__(self):
        self.connect = pymysql.connect()