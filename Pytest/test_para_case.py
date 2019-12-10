#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_para_case.py
@Time    :   2019/12/7下午4:02
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest
from datetime import datetime, timedelta


para_data = [
    (datetime(2019, 12, 7), datetime(2019, 12, 8), timedelta(1)),
    (datetime(2019, 12, 7), datetime(2019, 12, 8), timedelta(-1))
]


@pytest.mark.parametrize("a, b, excepted", para_data)
def test_timedistance_v0(a, b, excepted):
    diff = a - b
    assert diff == excepted


def ifdn(val):
    if isinstance(val, (datetime,)):
        # note this wouldn't show any hours/minutes/seconds
        return val.strftime('%Y%m%d')


@pytest.mark.parametrize("a,b,expected", para_data, ids=ifdn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected