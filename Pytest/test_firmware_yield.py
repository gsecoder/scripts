#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_firmware_yield.py
@Time    :   2019/12/919:06
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest

@pytest.fixture(scope="function")
def login():
    print("登录成功\n")
    yield
    print("注销登录\n")
    
    
def test_print():
    print("不会执行")
    
    
def test_view_info(login):
    print("执行测试\n")
    
    
if __name__ == "__main__":
    pytest.main(["test_firmware_yield.py", "-s"])
