#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   10_workpath_os_path.py
@Time    :   2019/12/2011:01
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :
"""

import os
import datetime

# 返回目录
print("返回当前执行文件的目录：%s" % os.path.dirname(__file__))
print(os.path.dirname("返回当前文件的工作空间目录：%s" % os.path.dirname(__file__)))

# 返回当前工作目录
print("返回当前工作目录：%s" % print(os.getcwd()))

# 判断路径是否存在
pwd1 = os.path.dirname(__file__)
pwd2 = "OperateFile"
print("如果路径存在，返回True：%s" % os.path.exists(pwd1))
print("如果路径存在，返回False：%s" % os.path.exists(pwd2))

# 返回一个绝对路径
print("返回一个绝对路径：%s, 注意它的盘符是当前操作系统的默认盘符" % os.path.abspath(pwd1))

# 返回路径的最后一部分
print("返回路径的最后一部分：%s" % os.path.basename(pwd1))

# 返回文件名
print("返回文件名 %s" % os.path.basename(__file__))

# 将路径切割成头和尾的一个元组
print("将路径切割成头和尾的一个元组：(%s, %s)" % os.path.split(pwd1))

# 拼接一个路径
print("拼接一个路径：%s" % os.path.join("D:\MySpace\Python\BasicPython\OperateFile", r"JoinFile"))


# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# 如果想要动态创建一个时间戳目录，来动态存放程序日志
# 1.为了避免程序找不到目录尴尬, 首先确定当前程序的工作空间
CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
print("当前程序的工作目录：%s" % CURRENT_DIR)
# 2.生成时间戳
nowTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print("程序执行的当前时间戳：%s" % nowTime)
# 3.拼接存放日志的目录
LOG_PATH = CURRENT_DIR + "/OperateFile/log/" + nowTime + "/"
print(LOG_PATH)
# 4.判断存放日志的目录LOG_PATH是否存在，不存在的话就就创建该目录
isExists = os.path.exists(LOG_PATH)
if not isExists:
    os.mkdir(LOG_PATH)

