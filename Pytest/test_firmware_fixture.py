#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_firmware_fixture.py
@Time    :   2019/12/917:33
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest

@pytest.fixture(scope="function")
def login():
    print("登录")
    

def test_print():
    print("执行打印\n")
    
    
def test_login_person(login):
    print("欢迎进入我的空间\n")
    
    
if __name__ == "__main__":
    pytest.main(["test_firmware_fixture.py", '-s'])
