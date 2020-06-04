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
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)

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
            self.connect.commit()
            print("创建表成功")
        except pymysql.DatabaseError as e:
            print("error: ", e.args)
        finally:
            self.connect.close()

    """
        执行数据的增、删、改、查语句
    """
    def execute_sql(self, method, sql_param, *args):
        try:
            if method == "select":
                self.cursor.execute(sql_param, *args)
                result = self.cursor.fetchall()
                return result
                # print("查询结果为：", result)
            else:
                self.cursor.execute(sql_param, *args)
                self.connect.commit()
                print("{}操作成功".format(method))
        except Exception as e:
            print("error: ", e)
            self.connect.rollback()
        finally:
            # self.cursor.close()
            # self.connect.close()
            pass

if __name__ == "__main__":
    odb = OperateDatabase()

    create_table_sql = """ 
    CREATE TABLE IF NOT EXISTS %s (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增列',
    title VARCHAR(20) NOT NULL COMMENT '文章标题',
    content VARCHAR(50) NOT NULL COMMENT '文章内容',
    active INT NOT NULL DEFAULT 1 COMMENT '文章激活状态：1，激活；0，未激活'
    ) ENGINE=InnoDB DEFAULT CHARSET='utf8';
    """ % 'article'

    select_sql = " SELECT * FROM article WHERE title = %s;"

    insert_sql = " INSERT INTO article(title, content, active)  VALUES (%s, %s, %s);"

    delete_sql = " DELETE FROM article WHERE title = %s;"

    update_sql = " UPDATE article SET title = %s WHERE id = %s;"

    # odb.create_db('unittest_api')
    # odb.create_table(create_table_sql)
    odb.execute_sql('select', select_sql, ('aa', ))
    # odb.execute_sql('insert', insert_sql, ("a中文", "aa中文", 1))
    # odb.execute_sql('delete', delete_sql, ('1', ))
    # odb.execute_sql('update', update_sql, ('aa', 4))
