#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : get_api_data.py
__time__    : 2020/6/20 17:09
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__description__: 通过获取数据库中的数据并传参，并传参给接口
"""

from unittest_api.get_database_cases import GetDbCases
import requests
from util.format_data import FormatData
import json

class GetApiData(object):
    def __init__(self):
        # 初始化数据库操作
        self.gdc = GetDbCases()

        # 初始化数据转换
        self.fd = FormatData

    def get_api_data(self):
        cases_result = self.gdc.get_cases()
        # print(cases_result)
        for item in cases_result:
            if item["is_execute"] == 1:
                # print(item)
                base_host = item["base_host"]
                api_name = item["api_name"]
                headers = self.fd.strdict_to_dict(item["headers"])
                # print("base_host ", base_host)
                # print("api_name ", api_name)
                # print("headers ", headers)
                # print("url: ", base_host+api_name)
                res = requests.get(
                    url=base_host + api_name + "query/",
                    headers=headers
                ).text.encode('utf-8').decode('unicode_escape')
                res = self.fd.strdict_to_dict(res)
                return res["articles"]
                # print("api_result: ", res["articles"])


if __name__ == '__main__':
    gai = GetApiData()
    gai.get_api_data()

"sql_execute_result:  " \
"[{'id': 4, 'title': 'aa', 'content': 'aa', 'active': 1}," \
" {'id': 5, 'title': 'a中文', 'content': 'aa中文', 'active': 1}," \
" {'id': 6, 'title': 'aa', 'content': 'aa2', 'active': 0}]"
""