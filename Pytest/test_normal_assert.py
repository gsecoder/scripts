#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_normal_assert.py
@Time    :   2019/12/7下午6:25
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""


def func():
    return 3


def test_func_1():
    assert func() == 3


def test_func_2():
    assert func() == 4
