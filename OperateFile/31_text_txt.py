#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   31_text_txt.py
@Time    :   2019/12/2217:20
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

file_name = "../OperateFile/data/txt.txt"
fr = open(file_name, 'r', encoding="utf-8")
fw = open(file_name, 'w', encoding="utf-8")
fa = open(file_name, 'a', encoding="utf-8")


def load_txt():
    print(fr.read())


def read_txt_byte(n):
    print(fr.read(n))


def read_line():
    print(fr.readline())

def read_lines():
    print(fr.readlines())
    
def write_txt(message):
    """
    :param message: 写入的数据
    :return: 返回写入的字符的长度
    """
    print(fw.write(message))
    
def write_lines(*args):
    print(fa.writelines(args))


def close_txt(self):
    fr.close()
    print("关闭读取文件句柄")
        
    
    

if __name__ == "__main__":
    file_name_1 = './data/txt1.txt'
    # write_txt("sjkjk")
    text_lists = "[1, 2, 3]"
    write_lines(text_lists)
    # print(ot.close_txt())