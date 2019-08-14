#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   61_OOPConcept.py
@Time    :   2019/7/23 18:09
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   面向对象编程概念
"""

# here put the import lib
# 1. 类
class OOPObject(object):
    # 5.类变量：定义在类中，方法之外的变量
    phone = 123456789
    address = "memory"

    # __init__方法的类在实例化的时候，会自动调用该方法，并传递对应的参数
    def __init__(self, name, age):
        # 4.实例变量，name 和 age就是实例变量
        self.name = name
        self.age = age

    # 7.实例方法
    def o_method(self):
        print("{0}:{1}".format(self.name, self.age))

    # 8.静态方法：不需要实例化就可以有类执行的方法
    @staticmethod
    def static_method():
        print("我是静态方法")

    # 9.类方法：类方法是将类本身作为对象进行操作的方法
    # 采用@classmethod装饰，至少传入一个cls（指类本身，类似于self）参数。
    # 执行类方法时，自动将调用该方法的类赋值给cls。
    # 使用类名.类方法的调用方式（也可以使用实例名.类方法的方式调用）
    @classmethod
    def class_method(cls):
        print("我是类方法")


# 2.实例
# 3.实例化---这个过程
o1 = OOPObject("oj", 23)
# 实例方法的调用
o1.o_method()


# （6）数据成员：类变量、实例变量、方法、类方法、静态方法和属性等的统称

# 静态方法的调用
OOPObject.static_method()


# 类方法
OOPObject.class_method()

