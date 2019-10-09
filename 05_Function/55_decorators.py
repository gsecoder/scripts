#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   55_decorators.py
@Time    :   2019/10/8 16:07
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. 装饰器示例
def authority(function_to_decorate):
    def auth():
        username = input("请输入用户名：")
        password = input("请输入用户密码：")
        if username == 'crisimple' and password == '123456':
            print("......认证成功......")
            function_to_decorate()
        else:
            print("......认证失败......")
    return auth

@authority
def view_space():
    print("......欢迎进入哔哩哔哩个人空间......")


# 2. 带固定参数的装饰器
def message_auth(function_to_decorate):
    def auth(user, passwd):
        username = input("请输入用户名：")
        password = input("请输入用户密码：")
        if username == user and password == passwd:
            print("......认证成功......")
            function_to_decorate(user, passwd)
        else:
            print("......认证失败......")
    return auth

@message_auth
def message(user, passwd):
    print("......您可以查看您的消息了......")


# 3. 无固定参数的装饰器
def pay_auth(function_to_decorate):
    def auth(*args, **kwargs):
        input("=====请输入你的动态口令=====: ")
        function_to_decorate(*args, **kwargs)
    return auth

@pay_auth
def pay(a, b, c):
    print("......您的账户余额为动态口令之和：%s" % (a+b+c))


# 4. 多个装饰器装饰同一函数
# 对于Python中的”@”语法糖，装饰器的调用顺序与使用 @ 语法糖声明的顺序相反。
def first_decorator(function_to_decorator):
    def wrapper():
        print("This is first decorator01")
        function_to_decorator()
        print("End of the first decorator01")
    return wrapper

def second_decorator(function_to_decorator):
    def wrapper():
        print("This is second decorator02")
        function_to_decorator()
        print("End of the second decorator02")
    return wrapper

@first_decorator
@second_decorator
def func_decorator():
    print("...【This is to be decorated function】...")


# 5. Python内置装饰器
class Foo(object):
    def __init__(self):
        self.name = 'zha nan'
        self.age = '23'

    # 不用传递self对象，就相当于是个普通方法
    @staticmethod
    def direct_call():
        print("类静态方法，可以在类不进行实例化的情况下调用，可以不用传self参数了，看到这句话就说明了这个道理")

    # 使用classmethod装饰器装饰后，方法的第一个参数是类对象；调用类方法不需要创建类的实例。classmethod也是一个类，所以classmethod是一个类装饰器。
    @classmethod
    def class_method(cls):
        print(cls.direct_call)

    # 对于一个类的属性，python的访问是没有限制的，但有时候我们需要对属性的访问加以限制，property可以胜任
    # property是一个类，它有三个方法，deleter，setter，getter，有两种使用方式。
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, set_num):
        return self.name == set_num

    @name.deleter
    def name(self):
        del self.name


from abc import abstractclassmethod, ABCMeta
# 一个类中的任何方法被abstractmethod装饰后，这个类不能实例化并且子类必须实现被abstractmethod装饰的方法
class ChildFoo(abstractmethod=ABCMeta):
    @abstractclassmethod
    def eat(cls):
        pass



if __name__ == "__main__":
    # view_space()
    # print("view_space.__name__ is: ", view_space.__name__)

    # message('crisimple', '123456')

    # pay(123, 456, 789)

    # func_decorator()

    Foo.direct_call()
    Foo.class_method()
