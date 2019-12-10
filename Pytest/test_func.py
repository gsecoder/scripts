#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_func.py
@Time    :   2019/12/7下午2:44
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
