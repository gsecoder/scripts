#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : format_data.py 
__author__ : crisimple
__date__   : 2020-06-04 16:07
__function__:
    strtuple_to_tuple(a) -- 字符串形式的元组转换成元组
    将字符串形式的字典专属为字典
"""
import json

class FormatData(object):

    def __init__(self):
        pass

    @staticmethod
    def strtuple_to_tuple(a):
        # strtuple = args
        # print("type of a", type(a))
        temp = a.replace('(', '').replace(')', '')
        strtuple = tuple(
            [i for i in temp.split(',')]
        )
        return strtuple

<<<<<<< HEAD
    def strdict_to_dict(b):
        # print("type of b", type(b))
        dict_info = json.loads(b)
        # print("type of temp: ", type(dict_info))
        return dict_info
=======
    @staticmethod
    def strdict_to_dict(b):
        temp = json.loads(b)
        return temp

>>>>>>> 9195aa4c97d9c0804db903427b80055c54654196


if __name__ == "__main__":
    fd = FormatData

    # aa = '(aa, 0)'
    # print("type of aa", type(aa))
    # print(fd.strtuple_to_tuple(aa))
    # print("type of fd.strtuple_to_tuple(aa)", type(fd.strtuple_to_tuple(aa)))

<<<<<<< HEAD
    bb = '{"a": 22, "b": 23}'
    print(fd.strdict_to_dict(bb))
=======
    bb = '{"aa":11, "bb":22}'
    fd_dict = fd.strdict_to_dict(bb)
    print("type of fd_dict: ", type(fd_dict))
    print("fd_dict: ", fd_dict)
>>>>>>> 9195aa4c97d9c0804db903427b80055c54654196

