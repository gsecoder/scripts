#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_updown_context.py
@Time    :   2019/12/1013:58
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest


def test_up_down():
    print("start......")
    set1 = set('1223')
    set2 = set('321')
    assert set1 == set2


# if __name__ == "__main__":
#     pytest.main(["test_updown_context.py", '-s'])
