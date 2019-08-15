#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   32_loopStructure.py
@Time    :   2019/07/21 19:43:10
@Author  :   Crisimple 
@Version :   1.0
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2016-2019, Micro-Circle
@Desc    :   None
'''

# here put the import lib
# 1. for...in...
list1 = [1, 2, 3, 4, 5, 2, 4, 7, 9, 0]
count = 0
for i in list1:
    if i == 2:
        count += 1
print("count: ", count)

# 2.嵌套for循环
# 乘法表
result = 0
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + '*' + str(i) + '=' + str(i*j) + '', end=' ')
    print(' ')


# 3.while循环
num = 1
while num <= 5:
    print("num：", num)
    num += 1
