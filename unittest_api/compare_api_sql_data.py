#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : compare_api_sql_data.py
__time__    : 2020/6/20 18:04
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__description__: 将 get_api_data 获取的接口返回结果
和 get_case_data 执行用例SQL返回的结果进行对比
"""
from unittest_api.get_case_data import GetCaseData
from unittest_api.get_api_data import GetApiData
from util.compare_json import CompareJson

class CompareData():

    def __init__(self):
        self.gad = GetApiData()
        self.gcd = GetCaseData()

    @staticmethod
    def compare_json(src_data, dst_data):
        # 比较的两个 json 的类型为 dict
        if isinstance(src_data, dict):
            for key in dst_data:
                if key not in src_data:
                    print("遍历dst_json：src_json不存在 %s，dst_json[%s] = %s" % (key, key, dst_data[key] ))
            for key in src_data:
                if key in dst_data:
                    if src_data[key] == dst_data[key]:
                        CompareJson.compare_json(src_data[key], dst_data[key])
                        # print("src_json[%s]=%s 【等于】 dst_json[%s]=%s" % (key, src_json[key], key, dst_json[key]))
                    else:
                        print("src_json[%s]=%s 【不等于】 dst_json[%s]=%s" % (key, src_data[key], key, dst_data[key]))
                else:
                    print("遍历src_json：dst_json不存在 %s，src_json[%s] = %s" % (key, key, src_data[key]))
        elif isinstance(src_data, (list, tuple)):
            if len(src_data) == len(dst_data):
                for key in range(len(src_data)):
                    if src_data[key] == dst_data[key]:
                        CompareJson.compare_json(src_data[key], dst_data[key])
                    else:
                        print("src_json[%s]=%s 【不等于】 dst_json[%s]=%s" % (key, src_data[key], key, dst_data[key]))
            else:
                print("len(%s)=%s 【不等于】 len(%s)=%s" % (src_data, len(src_data), dst_data, len(dst_data)))
        else:
            if str(src_data) == str(dst_data):
                print("%s【等于】%s" % (src_data, dst_data))
            else:
                print("%s【不等于】%s" % (src_data, dst_data))


if __name__ == '__main__':
    cd = CompareData()
    api_data = cd.gad.get_api_data()
    sql_data = cd.gcd.get_case_data()

    cd.compare_json(api_data, sql_data)
    # print(api_data)
    # print(sql_data)