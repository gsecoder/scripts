#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : run_sql.py
__author__ : crisimple
__date__   : 2020-06-01 16:54
__function__:
    读取数据模块
    可以读取 mysql 中数据
    可以读取 ini 文件中的数据
"""

from util.read_sql import ReadSql

class RunSql(object):

    def __init__(self):
        self.rs = ReadSql()

    def run_sql(self, method, *args):
        for index in self.rs.json_data:
            result = self.rs.select_sql(method, index, *args)
            print(result)

if __name__ == "__main__":
    rsl = RunSql()
    rsl.run_sql('select', (4, ))
