#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   compare_json_subset.py
@Time    :   2020/3/4下午1:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :
需求描述：
json_a = {
    "a": 1,
    "b": 2,
}

json_b = {
    "a": 1,
    "b": 2,
    "c": {
        "aa": 1,
        "bb": 1
    }
}
"""

import json

def compare_json_subset(json_1, json_2):
    # 若为 dict 格式
    if isinstance(json_1, dict) and isinstance(json_2, dict):
        # 遍历 json_1 中的每一个 key_1
        for key_2 in json_2:
            if key_2 not in json_1:
                print("json_1 中不存在 %s: %s这对值" % (key_2, json_2[key_2]))

        # 遍历 json_2 中的每一个 key_2
        for key_1 in json_1:
            if key_1 in json_2:
                if json_2[key_1] == json_1[key_1] and len(json_1) <= len(json_2):
                    print("%s 是 %s 的子集" % (json_1, json_2))
                else:
                    print("%s 不是 %s 的子集" % (json_1, json_2))
                compare_json_subset(json_1[key_1], json_2[key_1])
            else:
                print("json_2 中不存在 %s: %s这对值" % (key_1, json_1[key_1]))
    # 若为 list 格式
    elif isinstance(json_1, list)  and isinstance(json_2, list):
        if len(json_1) != len(json_2):
            print("json_1 和 json_2 的长度分别为： %s, %s" % (len(json_1), len(json_2)))
        elif len(json_1) == len(json_2) and len(json_1) > 1:
            for index in range(len(json_1)):
                for json_1_list, json_2_list in zip(sorted(json_1[index]), sorted(json_2[index])):
                    print(zip(sorted(json_1[index]), sorted(json_2[index])))
                    compare_json_subset(json_1_list, json_2_list)
        else:
            for json_1_list, json_2_list in zip(sorted(json_1[index]), sorted(json_2[index])):
                compare_json_subset(json_1_list, json_2_list)
    # 若为 str 格式
    else:
        if str(json_1) != str(json_2):
            print("json_1 和 json_2 分别是： ", (json_1, json_2))


if __name__ == "__main__":
    json_dict_1 = {
        "a": 1,
        "b": 2,
        "d": 3,
        "e": 4
    }
    json_dict_2 = {
        "a": 1,
        "b": 2,
        "c": {
            "aa": 1,
            "bb": 1
        }
    }
    # compare_json_subset(json_dict_1, json_dict_2)

    json_list_1 = [
        "a", "b", "c"
    ]
    json_list_2 = [
        "a"
    ]
    # compare_json_subset(json_list_1, json_list_2)

    json_str_1 = "abc"
    json_str_2 = "a"
    compare_json_subset(json_str_1, json_str_2)