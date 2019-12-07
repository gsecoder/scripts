#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_class.py
@Time    :   2019/12/616:19
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   1.运行多个测试文件
                pytest 会运行 test_ 开头 或者 _test 结尾的文件，在当前目录和子目录中
             2.一个类下的多个用例的运行， pytest会找到 test_ 开头的方法
"""

import pytest


class TestClass(object):
    
    def test_one(self):
        print("one case...\n")
        x = "test"
        assert 'e' in x
        
    def test_two(self):
        print("two case...\n")
        x = "hello"
        assert hasattr(x, 'check')
     
     
if __name__ == "__main__":
    pytest.main()
