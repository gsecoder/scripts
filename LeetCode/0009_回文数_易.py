#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0009_回文数_易.py
@Time    :   2019/10/30 11:47
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路一: 1.将整数转化为字符串；
       2.如果是回文数的话，正反字符串是一样的，返回True；如果不是的话，字符串肯定不一样，返回False
"""
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


"""
思路二: 1.将整数反向处理;
       2.比较原数和处理过的数据，如果相等则是，否则不是
"""
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        m, n = x, 0
        while m:
            """
                " / "  表示浮点数除法，返回浮点结果;
                " // " 表示整数除法,返回不大于结果的一个最大的整数 
                " % "  表示除法的余数，又叫取模运算
           """
            n = n * 10 + m % 10
            m = m // 10

        if x == n:
            return True
        else:
            return False


if __name__ == "__main__":
    """
    测试用例一
    """
    s1 = Solution1()
    x1 = 12321
    # print(s1.isPalindrome(x=x1))

    """
    测试用例二
    """
    s2 = Solution2()
    x2 = -12321
    print(s2.isPalindrome(x=x2))

print(121 % 10)
print(121 // 10)
print(12 // 10)
print(1 // 10)

str1 = "soose"
print(str1[::-1])
