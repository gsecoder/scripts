#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : request_method.py 
__author__ : crisimple
__date__   : 2020-06-01 13:21
__function__:
    请求接口的时候，被请求的接口存在不同的请求方式
    每一次的请求都要去手动修改请求方式，很不方便
    将接口的多种请求方式进行封装，根据不同的请求方式进行传参实现不通过方式的请求
"""
import requests
import json

class RequestMethod():

    @staticmethod
    def request_method(request_type, api_url, headers=None, data=None):
        if request_type == "GET":
            response_result = requests.get(url=api_url, headers=headers, params=data)
        elif request_type == "POST":
            response_result = requests.post(url=api_url, headers=headers, params=data)
        elif request_type == "DELETE":
            response_result = requests.delete(url=api_url, headers=headers, params=data)
        else:
            response_result = json.dumps(
                {
                    "status": 1000,
                    "msg": "请求方法错误"
                }
            )
        return response_result


if __name__ == "__main__":
    re = RequestMethod()
    api_headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
        "Authorization": "Basic Y3Jpc2ltcGxlOjEyMzQ1Ng=="
    }
    response_data = re.request_method(
        request_type="GET",
        api_url='http://127.0.0.1:8000/article_api/' + 'query/',
        headers=api_headers)

    # 代码转码
    result_code = response_data.status_code
    result_text = response_data.text.encode('utf-8').decode('unicode_escape')
    print("result_code: ", result_code)
    print("result_text: ", result_text)
