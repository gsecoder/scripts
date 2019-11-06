#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0020_有效的括号.py
@Time    :   2019/11/6 17:12
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路一: 1. 将括号对放到字典里成为键值对(左边做键，右边做值)，新创建一个栈
       2. 判断要判断的字符串长度如果为奇数长度，毫无疑问返回False，如果不是奇数长度进行判断
       3. 循环遍历字符串，如果字符串中的字符在字典中，则将字典的的间入栈
       4. 如果栈中的弹出的的键对应到字段中和要判断的字符串的元素不相等的时候，说明不匹配了，返回False；
       5. 如果说栈的长度不等于 1 的话，说明判断的字符串的元素一直在入栈，没有弹出只有半括号
时间复杂度: O(n)
"""
class Solution1:
    def isValid(self, s: str) -> bool:
        dict_parenthese = {'{': '}', '(': ')', '[': ']', '?': '?'}
        stack = ['?']
        if len(s) % 2 == 1:
            return False
        else:
            for c in s:
                if c in dict_parenthese:
                    stack.append(c)
                elif dict_parenthese[stack.pop()] != c:
                    return False
            return len(stack) == 1


if __name__ == "__main__":
    s1 = Solution1()
    print(s1.isValid('))'))
