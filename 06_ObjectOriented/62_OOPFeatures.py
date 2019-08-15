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


# 1. 封装
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


# 2.继承
class FatherClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = '中国'

    def father_method(self):
        print('father is walking')

    def talk(self):
        print("I'am father. %s" % self.name)


class BoyClass(FatherClass):
    # 先继承再重构，反着来子类就不能继承父类的属性了
    def __init__(self, name, age, sex):
        # 继承父类的构造方法
        # 经典继承
        # FatherClass.__init__(self, name, age)
        # 新式类继承
        super(BoyClass, self).__init__(name, age)
        # 定义子类本身的属性
        self.sex = sex
        print(self.name, self.age, self.country, self.sex)

    def child_method(self):
        print('child is walking...')

    def talk(self):
        print("I'am child. %s" % self.name)


class GirlClass(FatherClass):
    pass


# 2.1 构造方法继承
# 子类构造方法继承父类构造方法过程如下：
#   实例化对象b ---> b调用子类的构造方法__init__() ---> 子类的构造方法__init__()继承父类的构造方法__init__() ---> 调用父类的构造方法__init__()
b = BoyClass('Boy', 25, 'male')
print(b.name)
print(b.age)
print(b.sex)
print(b.country)
# 2.2 子类重写父类方法
f = FatherClass('A', 30)
f.talk()
b.talk()


# 3.

