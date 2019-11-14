#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PyMySQLSwitchDatabases.py
@Time    :   2019/11/13 15:48
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pymysql

class SwitchDatabase(object):

    def connect_databases(self):
        # 创建连接数据库的连接
        """
            host='要连接的数据库IP',
            user='数据库用户名',
            password='数据库的密码',
            database='要连接的数据库',
            charset='utf8'
        """
        self.conn = pymysql.connect(
            host='129.28.170.125',
            user='root',
            password='Root@159357',
            database='PythonDatabases',
            charset='utf8'
        )

        return self.conn

        # # 得到一个操作MySQL的光标对象
        # 默认执行完毕返回的结果集以元组显示
        # cursor_tuple = conn.cursor()
        # # 执行完毕返回的结果以字典显示
        # cursor_dict = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # # 执行sql
        # cursor_tuple.execute(sql)
        # # 关闭光标对象
        # cursor_tuple.close()
        # cursor_dict.close()
        # # 关闭数据库连接
        # conn.close()

    def close_databases(self):
        try:
            if self.conn:
                return self.conn.close()
        except Exception as e:
            print("Error: %s" % e)


if __name__ == "__main__":
    sql = """
        SELECT * FROM PythonDatabases.news
    """
    sd = SwitchDatabase()
    cursor = sd.connect_databases().cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    sd.close_databases()

