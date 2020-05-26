#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : python_module.py 
__author__ : jiangheng
__date__   : 2020-05-26 15:52
__function__:
在代码执行的时候我们总会遇到 "ModuleNotFoundError: No module named 'mock_django_api.article_api'" 类似的错误，
为了以后的调试，花时间解决下这个烦人的问题
"""

import os
import sys

"""
os - 负责程序与操作系统的交互，提供了访问操作系统底层的接口
sys - 负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境
"""
current_path = os.path.abspath(os.path.dirname(__file__))
print("current_path: ", current_path)
root_path = os.path.split(current_path)[0]
print("root_path: ", root_path)
sys.path.append(root_path)

