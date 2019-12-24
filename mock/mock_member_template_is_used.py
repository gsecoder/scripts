#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   mock_member_template_is_used.py
@Time    :   2019/12/2416:53
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from mock.template_class import Template
from unittest import mock
import unittest


class TemplateTest(unittest.TestCase):
    
    def test_should_validate_method_calling(self):
    
        t = Template()

        t.get_age = mock.Mock(return_value=22)
        print("没有被调用过：%s" % t.get_age.assert_not_called())
        
        t.get_age()
        print("任意调用次数：%s" % t.get_age.assert_called())
        # t.get_age()
        print("只调用过一次：%s" % t.get_age.assert_called_once_with())
        print("只要调用过即可：%s" % t.get_age.assert_any_call())
        
        # 重置mock，相当于没有调过
        t.get_age.reset_mock()
        print("没有被调用过：%s" % t.get_age.assert_not_called())
        
        # called表示是否调用过
        self.assertEqual(t.get_age.called, False)
        
        # call_count可以返回调用的次数
        self.assertEqual(t.get_age.call_count, 0)

        t.get_age()
        self.assertEqual(t.get_age.called, True)
        self.assertEqual(t.get_age.call_count, 1)
        
        
        

if __name__ == "__main__":
    unittest.main()
