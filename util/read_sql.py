#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : read_sql.py
__time__    : 2020/6/2 22:56
__author__  : crisimple
__github__ :  https://crisimple.github.io/
    获取要执行的 sql 语句，并执行 sql 语句获取执行结果
"""
import json
from util.operate_database import OperateDatabase

class ReadSql(object):

    def __init__(self, json_file=None):
        if json_file:
            self.json_file = json_file
        else:
            self.json_file = '../data/sql.json'

        # 读取 json 中存放的 sql 语句
        with open(self.json_file, 'r', encoding='utf-8') as fp:
            self.json_data = json.load(fp)

        # 初始化数据库操作
        self.od = OperateDatabase()

    def select_sql(self, method):
        dict_result = {}
        for index, item in self.json_data.items():
            # print("item: ", item)
            result = self.od.execute_sql(method, item['sql'], item['args'])
            dict_result[index] = result
        return dict_result

    def commit_sql(self):
        pass


if __name__ == "__main__":
    rs = ReadSql()
    select_result = rs.select_sql('select')
    print(select_result)