#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PyMySQLDelete.py
@Time    :   2019/11/14 19:11
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.PyMySQLSwitchDatabases import SwitchDatabase


class DeleteData(object):

    def __init__(self):
        self.sd = SwitchDatabase()
        self.cursor = self.sd.connect_databases().cursor()

    def delete_data(self, sql, data):
        try:
            self.cursor.execute(sql, data)
            self.sd.conn.commit()
        except Exception as e:
            print("Error: %s" % e)
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.sd.close_databases()


if __name__ == "__main__":
    sql_ele = """
        DELETE FROM PythonDatabases.news WHERE id = %s
    """
    data_ele = (21, )
    dd = DeleteData()
    dd.delete_data(sql=sql_ele, data=data_ele)