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
    这个模块可以用来集成做sql执行结果的执行工具
"""
import json

from util.read_sql import ReadSql

class RunSql(object):

    def __init__(self):
        self.rs = ReadSql()

    def run_sql(self):
        sql_select_result = self.rs.select_sql(method='select', which_args='query_condition')
        print(json.dumps(
            sql_select_result,
            indent=4,
            ensure_ascii=False
        ))

if __name__ == "__main__":
    rsl = RunSql()
    rsl.run_sql()
