#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_warns.py
@Time    :   2019/12/1013:54
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest
import warnings


def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)

