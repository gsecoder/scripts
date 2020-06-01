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
        self.connect = pymysql.connect(
            host='129.28.170.125',
            user='root',
            passwd='159357',
            port=3306,
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def create_db(self, db_name):
        try:
            self.cursor.execute(
                'CREATE DATABASE IF NOT EXISTS %s' % db_name
            )
            self.connect.select_db(db_name)
            self.connect.commit()
        except pymysql.DatabaseError as e:
            print(e.args)


if __name__ == "__main__":
    odb = OperateDatabase()
    odb.create_db('unittest_api')