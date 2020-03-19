#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_baidu.py
@Time    :   2019/12/2411:39
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from unittest import mock

import requests


def mock_baidu(base_url):
    results = requests.get(base_url)
    return results.status_code


url = "https://www.baidu.com"
# print(mock_baidu(url))


# 模拟请求百度，且返回值为500
mock_baidu = mock.Mock(return_code=500)
print("调用mock_baidu：%s" % mock_baidu(url))
print("调用mock_baidu：%s" % mock_baidu(url))
print("查看是否被调用：%s" % mock_baidu.called)
print("查看被调用的次数：%s" % mock_baidu.call_count)
print("查看被调用的返回值：%s" % mock_baidu.return_value)
print("查看被调用的返回值：%s" % mock_baidu.side_effect)
