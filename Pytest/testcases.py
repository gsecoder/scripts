#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   testcases.py
@Time    :   2019/12/616:19
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest

class TestClass(object):
    
    def test_one(self):
        x = "test"
        assert 'e' in x
        
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
     
     
if __name__ == "__main__":
    tc = TestClass()
    tc.test_one()
