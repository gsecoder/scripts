#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   取两个字符串中最大的公共子序列.py
@Time    :   2020/2/28上午11:17
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

str_1 = "abcdef"
str_2 = 'cd0123'

s1='超市很多人因为今天是大减价。'
s2='因为今天是大减价，所以超市有很多人。'
s11='也就是说遇冷夏。'
s22='也就是说遇到了冷夏。'


def findLcsStr(str1, str2):
    # 分别取两个字符串的长度
    lstr1 = len(str1)
    lstr2 = len(str2)

    # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]
    print(record)
    maxNum = 0  # 最长匹配长度
    max_end = 0  # 匹配的终止
    max_start = 0  # 匹配的起始位
    map_maxstr = {}  # key为开始位置，value为最大匹配字符串

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的开始位置

                    p = i + 1
                    max_start = i + 1 - maxNum
                    map_maxstr[max_start] = str1[p - maxNum:p]
                    maxNum = 0
        # return str1[p - maxNum:p], maxNum
    return map_maxstr

map_maxstr={}
map_maxstr = findLcsStr(s1, s2)#返回匹配字符串
for m in map_maxstr:
     print(map_maxstr.get(m))


map_maxstr = findLcsStr(s22, s11)#返回匹配字符串
for m in map_maxstr:
     print(map_maxstr.get(m))


# findLcsStr(str_1, str_2)