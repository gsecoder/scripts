#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PyMySQLSelect.py
@Time    :   2019/11/14 15:15
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PyMySQLSwitchDatabases import SwitchDatabase

class SelectData(object):

    def __init__(self):
        self.sd = SwitchDatabase()
        self.cursor = self.sd.connect_databases().cursor()

    def get_one(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        print(results)
        self.cursor.close()
        self.sd.close_databases()

    def get_all(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results)
        self.cursor.close()
        self.sd.close_databases()


if __name__ == "__main__":
    sql_ele = """
        SELECT * FROM PythonDatabases.news
    """
    sed = SelectData()
    # sed.get_one(sql_ele)
    sed.get_all(sql_ele)
