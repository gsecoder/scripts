#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_member_template_para_value.py
@Time    :   2019/12/2416:34
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import unittest
from unittest import mock

from mock.template_class import Template


class TemplateTest(unittest.TestCase):
    
    @unittest.skip("先跳吧")
    def test_get_full_name(self):
        t = Template()
        
        values = {
            ('cris', 'simple'): 'cris simple',
            ('xiao', 'ming'): 'xiao ming'
        }
        
        t.get_full_name = mock.Mock(side_effect=lambda x, y: values[(x, y)])
        self.assertEqual(t.get_full_name('cris', 'simple'), 'cris simple')
        self.assertEqual(t.get_full_name('xiao', 'ming'), 'xiao ming')
        
    def test_raise_get_age(self):
        t = Template()
        t.get_age = mock.Mock(side_effect=TypeError("integer type"))
        self.assertRaises(TypeError, t.get_age)
        

if __name__ == "__main__":
    unittest.main()
