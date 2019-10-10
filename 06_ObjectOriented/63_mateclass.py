#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   63_mateclass.py
@Time    :   2019/10/9 18:43
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 默认的元类type实例化出一个对象Foo，实例化的结果也是一个对象
class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating." % self.name)


f1 = Foo('mi', 9)


number = 12
dicts = {
    "name": "crisimple",
    "age": 23
}


print("number的ID是：", id(number))
print("dicts的ID是：", id(dicts))
print("number的type是：", type(number))
print("dicts的type是：", type(dicts))

print("Foo的ID是：", id(Foo))
print("Foo的type是：", type(Foo))      # Foo的type是： <class 'type'>
print("f1的ID是：", id(f1))
print("f1的type是：", type(f1))        # f1的type是： <class '__main__.Foo'>
# --------------------------------------
# instance ---[instance of]---> class ---[instance of]---> metaclass
#  f1     ---------------->  Foo  -------------->  type【type就是元类，元类自己也是对象】


Person = type("Person", (object, ), {"live": True, "name": 'crisimple'})
print(type(Person))
p1 = Person()
print(type(p1))
