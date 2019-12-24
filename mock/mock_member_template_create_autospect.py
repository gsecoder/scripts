#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_member_template_create_autospect.py
@Time    :   2019/12/2416:00
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   校验参数个数，再返回固定值
"""

from mock.template_class import Template
import unittest
from unittest import mock

class TemplateTest(unittest.TestCase):
    
    def test_get_full_name(self):
        t = Template()
        
        # 校验参数需要用create_autospec模块方法
        t.get_full_name = mock.create_autospec(t.get_full_name, return_value="cris simple")
        self.assertEqual(t.get_full_name('1', '2'), "cris simple")
        
        self.assertEqual(t.get_full_name('1', '2'), 'cris')
        
        
if __name__ == "__main__":
    unittest.main()
