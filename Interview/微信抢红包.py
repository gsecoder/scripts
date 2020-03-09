#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   微信抢红包.py
@Time    :   2020/2/28下午5:45
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import random


def qiang_redpackage(money_count, people_count):
    # 抢到红包的人的个数
    for i in people_count:
        j = 0
        while j <= people_count:
            # 已抢到红包额度初始化
            random_money_count = 0
            # 随机生成每个人的能抢到的红包额
            random_money = money_count - random.randint(1, money_count)
            # 抢到的红包额度
            random_money_count += random_money
            if random_money_count == money_count and j == people_count:
                print("红包已抢完")
            else:
                print("第 %s 个人抢到 %s，还有 %s 个人没有抢" % (i, money_count, j))
            # 累计抢到红包的人数
            j += 1


if __name__ == "__main__":
    money_count_1 = 100
    people_count_1 = 3
    qiang_redpackage(money_count_1, people_count_1)