#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0014_最长公共前缀,py
@Time    :   2019/11/4 16:34
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
from typing import List

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
内置函数: zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
思路一: 1.利用zip() 函数将字符串列表打包成一个个元组;
       2.因为是共同的前缀， 所以用集合set将元组去重;
       3.如果说去重后的结合长度==1, 则说明是字符串共有的元素，则进行字符拼接，如果不是则推出循环
时间复杂度: O(n) 
"""
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        @param strs: 字符串列表
        @return: 公共的字符串前缀
        print(i)
        print(set(i))
        print(len(set(i)))
        """
        s = ""
        for i in zip(*strs):
            # 因为set具有天然的去重性
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


if __name__ == "__main__":
    s1 = Solution1()
    print(s1.longestCommonPrefix(['flower', 'fly', 'flay']))

