#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PyMySQLSpringboardConnect.py
@Time    :   2019/11/13 19:07
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pymysql
from sshtunnel import SSHTunnelForwarder

def write_log(message, file_name="item_count.txt"):
    mylog = open(file_name, mode='a', encoding='utf-8')
    print(message, file=mylog)
    mylog.close()


class ConnectMysql:
    # XXX.XXX.XXX.230数据库是通过跳板机来进行连接的
    def __init__(self):
        self.db_host = "XXX.XXX.XXX.230要连接的数据库"
        self.db_port = 22
        self.db_user = "用户名"
        self.db_password = "数据库的密码"

        self.get_connect()

    # 建立连接
    def get_connect(self):
        self.server = SSHTunnelForwarder(
            (self.db_host, self.db_port),
            ssh_username="跳板机的用户名",
            ssh_password="跳板机的密码",
            remote_bind_address=('127.0.0.1', 3306)
        )
        self.server.start()

        self.connect = pymysql.connect(
            host="127.0.0.1",
            port=self.server.local_bind_port,
            user=self.db_user,
            password=self.db_password,
            db='btzc',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def close_connect(self):
        try:
            if self.connect:
                self.connect.close()
        except Exception as e:
            print("Error %s" % e)
