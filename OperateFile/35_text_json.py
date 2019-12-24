#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   35_text_json.py
@Time    :   2019/12/239:55
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :
-----------
    json.loads针对内存对象，即将Python内置数据序列化为字串
    json.load针对文件句柄，主要是针对读取文件
    
    json.dumps针对的是内存中的数据，将内存中的数据转换成json格式在控制台显示
    json.dump针对的是文件数据，将转换后的json数据输出到文件中展示
-----------

"""

import os
import sys
import json

file_name = "../OperateFile/data/json.json"

json_list = '["foo", {"bar":["baz", null, 1.0, 2]}]'
json_dict = '{"a": 0, "b": 0, "c": 0}'

def loads_json(args):
    """
    :param args: 要解析的的数据，可以是
    :return:
    """
    result = json.loads(args)
    return result
    

def load_json(file_path=None):
    """
    :param file_path: 要加载解析的文件
    :return: 解析后的数据
    """
    my_json = open(file_path, 'r', encoding="utf-8")
    result = json.load(my_json)
    return result

def dumps_file_json(file_path=None):
    """
    现将文件中的数据读取到内存中，再从内存中读取，输出到控制台显示
    :param file_path: 要加载解析的文件
    :return: 解析后的格式化数据
    """
    my_json = open(file_path, 'r', encoding="utf-8")
    result = json.load(my_json)
    format_result = json.dumps(result, indent=4, ensure_ascii=False)
    return format_result

def dumps_args_json(args=None):
    """
    将内存中的数据转换为json格式，并排序
    :param args: 内存中的数据，数据类型可以是字符串、列表、字典
    :return: json数据
    """
    format_result = json.dumps(args, indent=4, ensure_ascii=False, sort_keys=True)
    return format_result

def dump_json(args_info=None, file_path=None):
    """
    将内存中的数据解析成json输出到文件中去
    :param args_info: 内存的数据，可以是字符串、列表、字典
    :param file_path: json要输出到的文件名称
    :return: 输出json数据文件
    """
    my_file = open(file_path, 'w')
    json.dump(args_info, my_file, indent=4)
 
 
    
if __name__ == "__main__":
    
    # 从内存中读取将json解析
    # print("将json解析成列表：%s" % loads_json(json_list))
    # print("数据类型为：%s" % type(loads_json(json_list)))
    # print("将json解析成字典：%s" % loads_json(json_dict))
    # print("数据类型为：%s" % type(loads_json(json_dict)))
    #
    # 从文件中读取解析json
    # print("读取文件中的json数据：%s" % load_json(file_path=file_name))
    # print("读取文件中的json数据的数据类型为：%s" % type(load_json(file_path=file_name)))

    # 将数据格式化成json数据格式
    # print("读取文件中的json数据：%s" % dumps_file_json(file_path=file_name))
    # print("数据类型为：%s" % type(dumps_file_json(file_path=file_name)))
    data_str = "\"foo\bar"
    data_list = ['foo', {'bar': ('baz', None, 1.0, 2)}]
    data_dict = {"c": 0, "b": 0, "a": 0}
    print("将字符串转换为json：%s" % dumps_args_json(data_str))
    print("数据类型为：%s" % type(dumps_args_json(data_str)))
    print("将列表转换为json：%s" % dumps_args_json(data_list))
    print("数据类型为：%s" % type(dumps_args_json(data_list)))
    print("将字段转换为json：%s" % dumps_args_json(data_list))
    print("数据类型为：%s" % type(dumps_args_json(data_list)))
    
    
    # args = [1, 2, 3, {'4': 5, '6': 7}]
    # file_name = "../OperateFile/data/dump_json.json"
    # dump_json(args, file_name)
