#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : format_data.py 
__author__ : crisimple
__date__   : 2020-06-04 16:07
__function__:
    字符串形式的元组转换成元组
"""

class FormatData(object):

    def __init__(self):
        pass

    def strtuple_to_tuple(a):
        # strtuple = args
        print("type of a", type(a))
        temp = a.replace('(', '').replace(')', '')
        strtuple = tuple(
            [i for i in temp.split(',')]
        )
        return strtuple


if __name__ == "__main__":
    fd = FormatData
    aa = '(aa, 0)'
    print("type of aa", type(aa))
    print(fd.strtuple_to_tuple(aa))
    print("type of fd.strtuple_to_tuple(aa)", type(fd.strtuple_to_tuple(aa)))

