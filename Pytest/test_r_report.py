#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_r_report.py
@Time    :   2019/12/1010:21
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest


@pytest.fixture
def error_fixture():
    assert 0
    
    
def test_ok():
    print("ok")
    
    
def test_fail():
    assert 0
    
    
def test_error(error_fixture):
    print("error")
    
    
def test_skip():
    pytest.skip("skip this test case...")
    
    
def test_xfail():
    pytest.xfail("xfailing this test")
    
    
@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
