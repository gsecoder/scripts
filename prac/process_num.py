#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : process_num.py
__time__    : 2020/6/24 9:30
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__resume__ : 
"""


def judge_sxh(args_num):
    nums = list(str(args_num))
    s = 0
    for num in nums:
        s += int(num) ** len(nums)
    if args_num == s:
        return args_num


def judge_perfect_num(args_num):
    s = 0
    for i in range(1, args_num):
        if args_num % i == 0 and i < args_num:
            s += i
    if s == args_num:
        return args_num

def judge_duicheng(args_num):
    args_num = str(args_num)
    if args_num[0] == args_num[3] and args_num[1] == args_num[2]:
        return args_num


if __name__ == '__main__':
    sxh_num = []
    for i in range(100, 1000):
        sxh = judge_sxh(i)
        if sxh is not None:
            sxh_num.append(sxh)
    # print(sxh_num)

    perfect_num = []
    for num in range(1, 1000):
        j = judge_perfect_num(num)
        if j is not None:
            perfect_num.append(j)
    # print(perfect_num)

    nums = 1330
    print(judge_duicheng(nums))
22