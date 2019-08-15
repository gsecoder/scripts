#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   52_exceptionHanding.py
@Time    :   2019/8/15 18:15
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. try...exception...finally异常处理
list_exception = [1, 2, 3]

try:
    for i in list_exception:
        print(list_exception[i+2])

    raise TypeError('....主动抛出异常...')
except IndexError as e:
    print("异常 %s 已经在这里被捕获了，下面再有异常处理就不再被捕获了" % e)
except Exception as e:
    print(e)
finally:
    print("程序执行结束，不管异常是否被捕获，这里一定始终会执行\n")


# 2. try...exception...else
else_exception = [1, 2, 3]
try:
    for i in [1, 4]:
        print(i)
except IndexError as e:
    print(e)
except SyntaxError as se:
    print(se)
else:
    print("只有再try语句里面的执行成功的时候，才会执行else里面的内容")


# 3.自定义异常
class EvaException(BaseException):
    def __int__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


# try:
#     raise EvaException("自定义错误")
# except EvaException as e:
#     print(e)


# 4. 断言
assert 1 == 1
try:
    assert 1 == 2
except AssertionError as e:
    print("看见我说明断言的判断条件是错误的，这个异常已经被我捕获了： %s" % e)



