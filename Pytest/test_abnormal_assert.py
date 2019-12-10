#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_abnormal_assert.py
@Time    :   2019/12/7下午6:41
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as e:
        1/0
    assert e.type == "RuntimeError"


def test_error_just():
    with pytest.raises(ZeroDivisionError) as e:
        1/0
    assert e.type == "RuntimeError"
