#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : get_database_cases.py
__time__    : 2020/6/20 11:31
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__description__: 获取存放在 mysql 数据库中的接口测试用例
"""
from util.operate_database import OperateDatabase

class GetDbCases(object):

    def __init__(self):
        """初始化数据库"""
        self.od = OperateDatabase()

    """ 
        获取 unittest.test_article_api 中存放的测试用例数据
        返回的每一行作为列表的一项
        列表的每一项又是一个小字典组成
    """
    def get_cases(self):
        sql_select = "SELECT * FROM test_article_api"
        result = self.od.execute_sql(
            method="select",
            sql_param=sql_select
        )
        return result


if __name__ == '__main__':
    gdc = GetDbCases()
    cases_result = gdc.get_cases()
    print(type(cases_result))
    print(type(cases_result[0]))
    print(cases_result[0]["case_sql"])
