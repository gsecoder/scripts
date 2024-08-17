#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__@author__ : secoder
__@cnblog__: https://www.cnblogs.com/secoder
__file__   : test2.py
__time__   : 2024/7/17 16:26
__describe__：
"""
            

def sameStr(s: str) -> bool:
    str_length = len(s)
    # 遍历所有可能的子串长度，从1到字符串长度的一半
    for i in range(1, str_length // 2 + 1):
        # 如果字符串的长度可以被当前子串长度整除，说明可能存在重复模式
        if str_length % i == 0:
            # 截取子串
            sub_str = s[:i]
            # 计算重复次数
            repeat_times = str_length // i
            # 如果相等，说明有重复的子串
            if sub_str * repeat_times == s:
                return True
    # 如果没有返回False
    return False


if __name__ == '__main__': 
    # 测试代码
    print(sameStr("abab")) 