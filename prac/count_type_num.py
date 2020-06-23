#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : count_type_num.py
__time__    : 2020/6/23 11:38
__author__  : 
__github__  : https://github.com/crisimple/  
__resume__  : None
"""

def count_type_num(args_list):
    positive_num = 0
    negative_num = 0
    for i in args_list:
        if i > 0:
            positive_num += 1
        elif i < 0:
            negative_num += 1
    return positive_num, negative_num

def count_type_num2(args_list):
    positive_list = [i for i in args_list if i > 0 ]
    negative_list = [i for i in args_list if i < 0]
    print("zheng", len(positive_list))
    print("fu", len(negative_list))



if __name__ == '__main__':
    list_sample = [1, -1, 2, -3, 0, 5, 7]

    print(count_type_num(list_sample))

    # count_type_num2(input_list_sample)

    str_sample = "Hello_Jupyter_Notebook"
    new_sample = str_sample.split("_")
    print(new_sample)
    print(type(new_sample))
    print("".join(new_sample))
