#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   31_fileOperate.py
@Time    :   2019/7/22 10:52
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# here put the import lib
# 1. 文件读取
# codecs模块：主要用来解决文件乱码的问题
import codecs

f_read = codecs.open('read_file.txt', 'rb', encoding="utf-8")
print("f_read: ", f_read.read())
f_read.close()


