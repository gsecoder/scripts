#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_member_template_value.py
@Time    :   2019/12/2414:30
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import unittest
from unittest import mock

from mock.template_class import Template


# ------------- mock --------------------
class TemplateTest(unittest.TestCase):
    # -------------- *** 1.使用mock类返回固定值 *** ----------------
    # @unittest.skip("第一个跳过")
    def test_get_age(self):
        t1 = Template()
        # 不mock时，get_age应返回10
        self.assertEqual(t1.get_age(), 11)
        # mock掉get_age()方法，让其返回22
        t1.get_age = mock.Mock(return_value=22)
        self.assertEqual(t1.get_age(), 22)

    # @unittest.skip("第二个跳过")
    def test_get_full_name(self):
        t2 = Template()
        # mock掉get_full_name
        t2.get_full_name = mock.Mock(return_value="Crisimple")
        self.assertEqual(t2.get_full_name(), "Cris")
        
        
if __name__ == "__main__":
    unittest.main()
