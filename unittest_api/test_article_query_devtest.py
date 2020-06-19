#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : test_article_query_devtest.py
__author__ : jiangheng
__date__   : 2020-06-05 9:27
__function__:
    文章接口查询测试
"""

import unittest
from util.read_ini import ReadIni
from util.read_sql import ReadSql
from util.request_method import RequestMethod
from util.format_data import FormatData
from util.read_sql import ReadSql

class TestArticleQuery(unittest.TestCase):

    def setUp(self):
        # 初始化时从 unittest_api.ini 文件中读取被测接口的配置文件
        ri = ReadIni(ini_file="../data/unittest_api.ini")
        self.base_url = ri.read_ini('article_api', 'base_url')
        api_headers_ini = ri.read_ini('article_api', 'article_headers')

        # 初始化数据格式化工具，因为从ini配置文件中读取的 headers 为字符串形式，没有办法取得 item 的值
        self.fd = FormatData
        self.api_headers = self.fd.strdict_to_dict(api_headers_ini)

        # 初始化时从 mysql.json 文件中读取被测接口的传参即测试用例数据
        # 由于插叙接口不用传参所以不用初始化

        # 初始化请求接口方法
        self.rm = RequestMethod()

        # 初始化执行 SQL 操作方法
        self.rs = ReadSql()

    def test_article_query(self):

        # 请求接口返回的值
        api_data = self.rm.request_method(
            request_type='GET',
            api_url=self.base_url + 'query/',
            headers=self.api_headers
        )
        result_text = api_data.text.encode('utf-8').decode('unicode_escape')
        print("type of result_text: ", result_text)

        # 请求数据库获取返回值
        sql_data = self.rs.select_sql('select')
        print(sql_data)

def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()