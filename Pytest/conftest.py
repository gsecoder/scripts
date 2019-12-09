#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   conftest.py
@Time    :   2019/12/919:24
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest

@pytest.fixture(scope="function")
def login():
    print("登录成功")

