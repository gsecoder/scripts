#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   compare_json_jsontools.py
@Time    :   2020/3/2下午2:54
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import json_tools

def compare_json(json_1, json_2):
    results = json_tools.diff(json_1, json_2)
    print(results)


if __name__ == "__main__":
    json_a = """
    {
        "a": 1,
        "b": 2,
        "c": {
            "aa": 1,
            "bb": 1
        }
    }
    """

    json_b = """
    {
        "a": 1,
        "c": {
            "aa": 1,
            "bb": 1
        }
    }
    """
    compare_json(json_a, json_b)



