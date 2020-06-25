#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : compare_json.py 
__author__ : crisimple
__date__   : 2020-06-03 9:47
__function__:
    比较得到的两个 json 数据
"""
import json

class CompareJson(object):
    # 类初始化的时候读取json文件中的数据
    def __init__(self, json_src_file=None, json_dst_file=None):
        with open(json_src_file, 'r', encoding='utf-8') as fp:
            self.src = json.load(fp)
        with open(json_dst_file, 'r', encoding='utf-8') as fp:
            self.dst = json.load(fp)

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


if __name__ == "__main__":
    src_file = '../data/src_json.json'
    dst_file = '../data/dst_json.json'
    cj = CompareJson(src_file, dst_file)
    # cj.compare_json(cj.src, cj.dst)

    src_list_data = [12, 22, 32, [1, 2]]
    dst_list_data = [12, 22, 32, [1, 3]]
    # cj.compare_json(src_list_data, dst_list_data)

    src_str_data = "qwqw"
    dst_str_data = "qw"
    cj.compare_json(src_str_data, dst_str_data)





