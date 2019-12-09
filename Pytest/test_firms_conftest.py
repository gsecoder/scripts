#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_firms_conftest.py
@Time    :   2019/12/920:11
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest

def test_print():
    print("print method")
    
    
def test_view_data(login):
    print("\n查看到数据...")
    

if __name__ == "__main__":
    pytest.main(["test_firms_conftest.py", "-s"])
