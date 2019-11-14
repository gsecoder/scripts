#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PyMySQLUpdate.py
@Time    :   2019/11/14 18:19
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PyMySQLSwitchDatabases import SwitchDatabase

class UpdateData(object):

    def __init__(self):
        self.sd = SwitchDatabase()
        self.cursor = self.sd.connect_databases().cursor()

    def update_one(self, sql, data):
        try:
            # sql
            self.cursor.execute(sql, data)
            self.sd.conn.commit()
        except Exception as e:
            print("Error: %s" % e)
        # 关闭游标
        self.cursor.close()
        self.sd.close_databases()

    def update_more(self, sql, data):
        try:
            self.cursor.executemany(sql, data)
            self.sd.conn.commit()
        except Exception as e:
            print("Error: %s" % e)
        # 关闭游标
        self.cursor.close()
        self.sd.close_databases()


if __name__ == "__main__":
    sql_ele_one = """
        UPDATE PythonDatabases.news
        SET title = %s, content = %s, types = %s
        WHERE id = %s; 
    """
    data_ele_one = ('news20', 'news20Content', 'baijia20', '20')

    sql_ele_more = """
        UPDATE PythonDatabases.news
        SET title = CASE
            WHEN id = %s THEN %s
            WHEN id = %s THEN %s
            WHEN id = %s THEN %s
            END
        WHERE id in (%s, %s, %s);
    """
    data_ele_more = (7, 'news7', 8, 'news8', 9, 'news9', 7, 8, 9)
    ud = UpdateData()
    ud.update_one(sql_ele_more, data_ele_more)

