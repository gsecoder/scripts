#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : run_unittest.py
__time__    : 2020/6/20 9:41
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__description__: 执行 unittest 框架构建的自动化接口测试用例
"""

from unittest_api.test_article_query import TestArticleQuery
import unittest

def run_unittest():
    # 构建测试套件
    suite = unittest.TestSuite()
    suite.addTest(TestArticleQuery("test_query_all"))
    suite.addTest(TestArticleQuery("test_query_condition"))

    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    run_unittest()



