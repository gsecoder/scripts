#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   62_OOPFeatures.py
@Time    :   2019/8/14 15:15
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

class ThisClass(object):
    class_name = 'This class'
    class_age = 12

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_class(self):
        print("{0}:{1}".format(self.name, self.age))


# 这就说明：外部不能直接调用类变量和类方法
# print(class_name)  NameError: name 'class_name' is not defined
# print_class()   NameError: name 'print_class' is not defined

# 使用：类.变量/方法，来访问类的变量或方法
print(ThisClass.class_name)
ThisClass.class_name = 'Change name value'
print(ThisClass.class_name)
ThisClass.class_add_attribute = 'Test add attribute'
print(ThisClass.class_add_attribute)
tc = ThisClass('A', 23)
print(tc.print_class())

