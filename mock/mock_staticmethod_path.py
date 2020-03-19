#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_staticmethod_path.py
@Time    :   2019/12/2417:40
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
    # 以字符串的形式列出静态方法的路径，在测试的参数里会自动得到一个Mock对象
    @mock.patch('mock.template_class.Template.get_age)')
    def test_get_age(self, mock_get_age):
        mock_get_age.return_value = 21
        
        self.assertEqual(Template.get_age(), 21)
        

if __name__ == "__main__":
    unittest.main()