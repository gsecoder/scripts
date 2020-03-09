#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   compare_json_equal.py
@Time    :   2020/3/3下午4:32
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :
https://www.sohu.com/a/272037922_741445
https://www.cnblogs.com/lovesqcc/p/5380142.html
https://www.cnblogs.com/wozijisun/p/10337040.html
"""

import json


def compare_json_1(json_1, json_2):
    # 将两个json转换成两个dict
    dict1 = json.loads(json_1)
    dict2 = json.loads(json_2)

    # 将两个字典按key排好序
    sort_dict1 = sorted(dict1)
    sort_dict2 = sorted(dict2)

    # zip()函数将两个字典对应的元素打包成元组
    for key1, key2 in zip(sort_dict1, sort_dict2):
        # 比较对应的元素的value是否相等

        if str(dict1[key1]) != str(dict2[key2]):
            print(key1, dict1[key1], key2, dict2[key2])
        else:
            # 如果相等的，继续进行比较
            compare_json_1(json_1[key1], json_2[key2])

def compare_json_2(json_1, json_2):
    if isinstance(json_1, dict):
        # 如果 json_1 为 dict 类型
        for key in json_2:
            if key not in json_1:
                print("%s 不存在 %s " % (json_1, key))
        for key in json_1:
            if key in json_2:
                compare_json(json_1[key], json_2[key])
                # print("%s 和 %s 相等" % (json_1, json_2))
    elif isinstance(json_1, list):
        if len(json_1) != len(json_2):
            print("%s 与 %s 的长度不相等")
        for json_1_list, json_2_list in zip(json_1, json_2):
            compare_json_2(json_1_list, json_2_list)
    else:
        if str(json_1) != str(json_2):
            print(json_1)

def compare_json_3(json_1, json_2):
    # 若为 dict 格式
    if isinstance(json_1, dict) and isinstance(json_2, dict):
        # 遍历循环 json_2 的元素
        for key_2 in json_2:
            # 如果 json_2 里的元素 key_2 不存在于 json_1 中
            if key_2 not in json_1:
                print("json_1 不存在 %s: %s" % (key_2, json_2[key_2]))
        for key_1 in json_1:
            if key_1 in json_2:
                if json_2[key_1] == json_1[key_1]:
                    # print("%s 与 %s 相等" % (json_2, json_1))
                    pass
                compare_json_3(json_1[key_1], json_2[key_1])
            else:
                print("json_2 不存在 %s: %s 元素" % (key_1, json_1[key_1]))
    # 若为 list 格式
    elif isinstance(json_1, list) and isinstance(json_2, list):
        if len(json_1) != len(json_2):
            print("json_1 和 json_2 的长度分别为： %s, %s" % (len(json_1), len(json_2)))
        if len(json_1) == len(json_2) and len(json_1) > 1:
            for index in range(len(json_1)):
                for json_1_list, json_2_list in zip(sorted(json_1[index]), sorted(json_2[index])):
                    compare_json_3(json_1_list, json_2_list)
        else:
            for json_1_list, json_2_list in zip(sorted(json_1[index]), sorted(json_2[index])):
                compare_json_3(json_1_list, json_2_list)
    # 若为 str 格式
    else:
        if str(json_1) != str(json_2):
            print("json_1 和 json_2 分别是： ", (json_1, json_2))


if __name__ == "__main__":
    json_a = {
        "a": 1,
        "b": 2,
        "d": "dd"
    }

    json_b = {
        "a": 1,
        "b": 2,
        "c": {
            "aa": 1,
            "bb": 1
        }
    }

    json_list_1 = [
        {
            "a": 1,
            "b": 2,
            "c": {
                "aa": 1,
                "bb": 1
            }
        }
    ]

    json_list_2 = [
        {
            "a": 1,
            "b": 2
        }
    ]


    # compare_json_1(json_a, json_b)
    # compare_json_2(json_a, json_b)
    # compare_json_3(json_a, json_b)

    json_str_1 = "abc"
    json_str_2 = "a"
    compare_json_3(json_str_1, json_str_2)




