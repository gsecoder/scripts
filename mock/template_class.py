#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   template_class.py
@Time    :   2019/12/2415:56
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

class Template(object):
    age = 11
    
    def __int__(self, age):
        self.age = age
        self.name = "AA"
    
    # 有参数
    def get_full_name(self, first_name, last_name):
        return first_name + '' + last_name
    
    # 无参数
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    # 静态方法
    @staticmethod
    def get_class_name():
        return Template.__name__
    

if __name__ == "__main__":
    """
    判断类是否含有某个属性：hasattr(Template, "age")
    """
    # t1 = Template()
    # print(t1.get_age())
    # # print(hasattr(Template, "age"))
    # # print(hasattr(Template, "name"))
    # print("1-------------------\n")
    
    print(Template.get_age)
