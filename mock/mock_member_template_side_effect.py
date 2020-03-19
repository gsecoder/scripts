#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_member_template_side_effect.py
@Time    :   2019/12/2416:15
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
    
    def test_get_age(self):
        t = Template()
        t.get_age = mock.Mock(side_effect=[10, 11, 12])
        
        self.assertEqual(t.get_age(), 10)
        self.assertEqual(t.get_age(), 11)
        self.assertEqual(t.get_age(), 12)
        

if __name__ == "__main__":
    unittest.main()