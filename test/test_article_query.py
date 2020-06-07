#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : test_article_query.py
__time__    : 2020/6/6 10:19
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import unittest
from util.request_method import RequestMethod
from util.format_data import FormatData
from util.read_ini import ReadIni
from util.read_sql import ReadSql
import json
from util.compare_json import CompareJson

class TestArticleQuery(unittest.TestCase):

    def setUp(self) -> None:
        # 初始化格式化
        self.fd = FormatData()

        # 初始化读取 ini 文件方法
        self.ri = ReadIni(ini_file="../data/unittest_api.ini")
        # 获取要请求接口的 url 和 headers
        self.base_request_type = self.ri.read_ini("article_api_query", "base_request_type")
        # print("base_request_type: ", self.base_request_type)
        self.base_url = self.ri.read_ini("article_api_query", "base_url")
        # print("base_url: ", self.base_url)
        self.base_headers = self.fd.strdict_to_dict(self.ri.read_ini("article_api_query", "base_headers"))

        # 初始化综合请求接口方法
        self.rm = RequestMethod()

        # 初始化执行SQL
        self.rs = ReadSql(json_file="../data/sql.json")

        # 初始化比较返回结果的方法
        self.cj = CompareJson



    def test_article_query(self):

        # 接口传参获取接口数据，鉴于 article_query 接口不用传参，所以就不用获取参数了
        api_data = self.rm.request_method(
            request_type=self.base_request_type,
            api_url=self.base_url + "query/",
            headers=self.base_headers
        )
        query_data_code = api_data.status_code
        query_data_text = json.loads(api_data.text.encode("utf-8").decode("unicode_escape"))
        api_data_text = query_data_text["articles"]

        # print("query_data_code: ", query_data_code)
        print("query_data_text: ", api_data_text)
        # return api_data

        # 传参读取数据库中的数据
        sql_data = self.rs.select_sql("select")
        sql_data_dict = sql_data["第一"]
        print("sql_data: ", type(sql_data))
        print("sql_data: ", sql_data_dict)

        # 比较 api 返回数据与 sql 查询逻辑返回数据对比
        self.cj.compare_json(api_data_text, sql_data_dict)



    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()