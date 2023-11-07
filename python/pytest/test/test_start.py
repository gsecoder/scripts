#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(x):
    return x + 1

def test_func():
    assert func(3) == 5
    
class TestClass:
    def test_one(self):
        x = "This"
        assert "h" in x
        
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")