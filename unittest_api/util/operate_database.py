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
            charset='utf8',
            db='unittest_api'
        )
        self.cursor = self.connect.cursor()

    """创建数据库"""
    def create_db(self, db_name):
        try:
            self.cursor.execute(
                'CREATE DATABASE IF NOT EXISTS %s' % db_name
            )
            self.connect.select_db(db_name)
            self.connect.commit()
        except pymysql.DatabaseError as e:
            print("error: ", e.args)

    """创建数据库表"""
    def create_table(self, table_sql):
        try:
            # 执行创建表 sql 语句
            self.cursor.execute(table_sql)
        except pymysql.DatabaseError as e:
            print("error: ", e.args)
        finally:
            self.connect.commit()
            return 0

if __name__ == "__main__":
    odb = OperateDatabase()

    create_table_sql = """ CREATE TABLE IF NOT EXISTS %s (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增列',
            title INT NOT NULL COMMENT '文章标题',
            content VARCHAR(50) NOT NULL COMMENT '文章内容',
            active INT NOT NULL DEFAULT 1 COMMENT '文章激活状态：1，激活；0，未激活'
        ) ENGINE=InnoDB DEFAULT CHARSET='utf8mb4';
    """ % 'article'
    # odb.create_db('unittest_api')
    odb.create_table(create_table_sql)