#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0013_罗马数字转整数.py
@Time    :   2019/11/4 10:51
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
思路一: 1.规律是罗马数字转换成整数时，如果前一个数大于等于后一个数，只需要加上前一个罗马数字对应的整数即可；
         如果前一个数小于后一个数的时候，减去前一个罗马数对应的整数；
       2.直到转换到倒数第一个数，由于最后一个数没有可比较对象了，所以加上最后一个数；
       3.将1和2的结果求和，即可得到最终转换完的整数结果
"""
class Solution1:
    def romanToInt(self, s: str) -> int:
        """
        @param s: 被转换的罗马数字
        @return: 转换后返回的
        """
        roman_num = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        sum_num = 0
        for i in range(len(s)-1):
            if roman_num[s[i]] >= roman_num[s[i+1]]:
                sum_num += roman_num[s[i]]
            else:
                sum_num -= roman_num[s[i]]
        last_num = s[len(s)-1]
        sum_num = sum_num + roman_num[last_num]
        return sum_num


if __name__ == "__main__":
    rt = Solution1()
    print(rt.romanToInt("XC"))
