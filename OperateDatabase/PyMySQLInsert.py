#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PyMySQLInsert.py
@Time    :   2019/11/14 15:52
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PyMySQLSwitchDatabases import SwitchDatabase


class InsertData(object):

    def __init__(self):
        self.sd = SwitchDatabase()
        self.cursor = self.sd.connect_databases().cursor()

    def insert_one(self, sql, data):
        try:
            self.cursor.execute(sql, data)
            print(sql)
            # 一定得提交数据
            self.sd.conn.commit()
        except Exception as e:
            print("Error: %s" % e)
            self.sd.conn.rollback()
        # 关闭游标
        self.cursor.close()
        self.sd.close_databases()

    def insert_more(self, sql, data):
        try:
            self.cursor.executemany(sql, data)
            self.sd.conn.commit()
        except Exception as e:
            print("Error: %s" % e)
            self.sd.conn.rollback()
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.sd.close_databases()


if __name__ == "__main__":
    sql_ele = """
        INSERT INTO PythonDatabases.news(title, content, types) VALUES(%s, %s, %s);
    """
    data_ele = (('news10', 'news10Content', 'baijia10'),
                ('news11', 'news11Content', 'baijia11'))
    ind = InsertData()
    # ind.insert_one(sql_ele, data_ele)
    ind.insert_more(sql_ele, data_ele)

