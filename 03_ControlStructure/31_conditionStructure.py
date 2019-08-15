#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   31_conditionStructure.py
@Time    :   2019/07/21 16:42:59
@Author  :   Crisimple 
@Version :   1.0
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2016-2019, Micro-Circle
@Desc    :   Python 有三大控制结构，分别是顺序结构、分支结构（选择结构）以及循环结构。
'''

# here put the import lib

# 1.顺序结构
# 顺序结构就是按照你写的代码顺序执行，也就是一条一条语句顺序执行。

# 2.分支结构
# 分支结构又称为选择结构，是程序代码根据判断条件选择执行特定的代码。如果条件为真，程序执行一部分代码；否则执行另一部分代码。
# 基本语法：
#     1、if
# 　　2、if...else
# 　　3、if...elif...else
# 　　4、if...elif...elif......else
# 　　5、if 嵌套

# 1.if 
a = 1
if a == 1:
    print("你的输出正确")

# 2.if...else...
a = 1
if a == 1:
    print("a的值为1")
else:
    print("a的值不为1")

# 3.if...elif...else...
a = 1
if a > 1:
    print("a的值大于1")
elif a == 1:
    print("a的值等于1")
else:
    print("a的值小于1")

# 4.if...elif...elif......else
a = 1
if a == 1:
    print("a的值为1")
elif a == 2:
    print("a的值为2")
elif a == 3:
    print("a的值为3")
else:
    print("a的值为不知道是什么")

# 5.if 嵌套
a = 1
b = 2
if a == 1:
    if b == 2:
        print("b的值为1")
    else:
        print("b的值不知道是什么")
else:
    print("a的值迷失了~")
