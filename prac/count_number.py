#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : count_number.py
__time__    : 2020/6/23 11:30
__author__  : 
__github__  : https://github.com/crisimple/  
__resume__  : None
"""

def count_number(args_str_sample):
    dic_str = {}
    args_str_sample = args_str_sample.replace(" ", "")
    for i in args_str_sample:
        if i in dic_str:
            dic_str[i] = args_str_sample.count(i)
        else:
            dic_str[i] = 1

    return dic_str


if __name__ == '__main__':
    str_sample = "111lovepython 777321"
    print(count_number(str_sample))

