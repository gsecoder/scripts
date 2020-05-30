# -*- encoding: utf-8 -*-
"""
__file__   : tests_article_api.py
__author__ : crisimple
__date__   : 2020-05-27 9:32
__function__: 测试 article_api 创建的接口
"""

import unittest
import requests
import json


class TestArticleApi(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://127.0.0.1:8000/article_api/'
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "Authorization": "Basic Y3Jpc2ltcGxlOjEyMzQ1Ng=="
        }

    # @unittest.skip("跳过查询")
    def test_query(self):
        results = requests.get(url=self.base_url+"query/", headers=self.headers)
        print(results.text)
        json_results = json.dumps(
            results.text,
            sort_keys=True,
            indent=4,
            ensure_ascii=False
        )
        print(json_results)

    @unittest.skip("跳过添加")
    def test_add(self):
        payloads = {
            "title": "脚本提交文章1",
            "content": "脚本提交文章1脚本提交文章1"
        }
        results = requests.post(url=self.base_url+"add/", headers=self.headers, json=payloads).text
        json_results = json.dumps(
            results,
            ensure_ascii=False
        )
        print(json_results)

    def test_update(self):
        payloads = {
            "title": "脚本提交文章1",
            "content": "修改文章1修改1"
        }
        results = requests.post(url=self.base_url+"update/27", headers=self.headers, json=payloads).text
        json_results = json.dumps(
            results,
            ensure_ascii=False
        )
        print(json_results)

    def test_delete(self):
        results = requests.delete(url=self.base_url+"delete/20", headers=self.headers).text
        json_results = json.dumps(
            results,
            ensure_ascii=False
        )
        print(json_results)


if __name__ == "__main__":
    unittest.main()

