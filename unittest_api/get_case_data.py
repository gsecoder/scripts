#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : get_case_data.py
__time__    : 2020/6/20 15:10
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__description__: 通过获取数据库中的 case_sql 并传参，得到每条 case 执行结果
"""
from unittest_api.get_database_cases import GetDbCases

class GetCaseData(object):
    def __init__(self):
        # 初始化获取 unittest_api.test_article_api 的测试数据
        self.gdc = GetDbCases()

        # 初始化数据库操作类
        self.od = self.gdc.od

    def get_case_data(self):
        cases_result = self.gdc.get_cases()
        # print(cases_result)

        # 得到每一行的用例数据
        for item in cases_result:
            # print(item)
            if item["is_execute"] == 1:
                case_sql = item["case_sql"]
                case_article_id = item["article_id"]
                case_article_title = item["article_title"]
                case_article_content = item["article_content"]
                case_article_status = item["article_status"]
                # print("case_sql", case_sql)
                # print("case_article_id", case_article_id)
                # print("case_article_title", case_article_title)
                # print("case_article_content", case_article_content)
                # print("case_article_status", case_article_status)

                sql_execute_result = self.od.execute_sql(
                    'select',
                    case_sql
                )
                # print("sql_execute_result: ", sql_execute_result)
                return sql_execute_result


if __name__ == '__main__':
    gcd = GetCaseData()
    gcd.get_case_data()