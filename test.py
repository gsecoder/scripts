#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__@author__ : secoder
__@cnblog__: https://www.cnblogs.com/secoder
__file__   : test
__time__   : 2024/7/16 15:32
__describe__：
"""  

def get_days(year, month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 判断是否是闰年,如何是润年的话，二月加1
    if(year % 4 == 0) and (year % 100 !=0):
        month_list[1] = 29
    
    # 求总的天数
    sum_day = sum(month_list[:month -1]) + day
    
    return sum_day


if __name__ == '__main__':
    year = 2024
    month = 7
    day = 14
    print(get_days(year, month, day))              