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
text = f_read.read()
print(type(text))
print("f_read: ", text)
f_read.close()


# 2. 写文件
f_write = codecs.open('write_file.txt', 'wb', encoding='utf-8')
f_write.write("********************\n")
f_write.write("<鹅>\n")
f_write.write("曲项向天歌\n")
f_write.write("白毛浮绿水\n")
f_write.close()



