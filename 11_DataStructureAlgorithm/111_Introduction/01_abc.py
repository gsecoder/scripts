#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   01_abc.py
@Time    :   2019/10/22 12:18
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc  :   如果 a + b +c = 1000 且 a**2 + b**2 = c**2（a, b, c均为自然数），求解a, b, c的所有组合
"""

import time

start_time = time.time()
print("程序开始执行时间: %s" % start_time)

# 算法一
# 时间复杂度：
#   T(n) = O(n*n*n) = O(n**3)
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d" % (a, b, c))


# 算法二
for a in range(1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))


# 算法三
# 时间复杂度：
#   T(n) = O(n*n(1+1))) = O(n**2)
for a in range(1001):
    for b in range(0, 1001 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))


end_time = time.time()
print("程序执行结束时间: %s" % end_time)

all_times = end_time - start_time
print("总耗时all_times: %s" % all_times)
print("执行完毕！")