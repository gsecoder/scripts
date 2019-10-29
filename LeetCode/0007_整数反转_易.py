#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0007_整数反转_易.py
@Time    :   2019/10/29 10:20
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路一:  (1)将整数取余操作并存入列表进行反转;
        (2)将反转后的列表进行累加输出;
        (3)区分大于0和小于0的情况
        (4)考虑数字范围及反转后溢出的问题
时间复杂度: O(n**2)
"""
class Solution1:
    def reverse(self, x: int) -> int:
        """
        @param x: 要被反转的整数
        @return: 返回的反转后的整数
        """
        arr = []
        a = 0
        if x > 0:
            for i in range(len(str(x))):
                arr.insert(i, (x // 10**i % 10))

            rra = list(reversed(arr))
            k = 1
            for j in range(len(rra)):
                a = rra[j]*(10**j) + a
                k = k + 1
            if -2**31 < a < 2**31-1:
                return a
            else:
                return 0
        elif x < 0:
            x = -x
            for i in range(len(str(x))):
                arr.insert(i, (x // 10**i % 10))

            rra = list(reversed(arr))
            k = 1
            for j in range(len(rra)):
                a = rra[j]*(10**j) + a
                k = k + 1
            if -2**31 < a < 2**31-1:
                return -a
            else:
                return 0
        else:
            return 0


"""
思路二：(1)将整数转换为字符串, 将字符串进行反转操作;
      (2)将反转后的字符串转换为整数;
      (3)转换后的整数考虑大于0小于0及0的情况;
      (4)考虑数字范围及反转后溢出的问题
时间复杂度: O(n)
"""
class Solution2:
    def reverse(self, x: int) -> int:
        pass

if __name__ == "__main__":
    """
    测试用例一
    """
    x1 = -4567
    s1 = Solution1()
    print(s1.reverse(x=x1))

    """
    测试用例二
    """

