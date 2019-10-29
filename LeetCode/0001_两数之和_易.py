#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0001_两数之和_易.py
@Time    :   2019/10/18 14:55
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :
"""
"""
------------------------------------------------------------------------------------------
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9，所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
-------------------------------------------------------------------------------------------
"""

from typing import List


"""
思路一： （1）从数组nums中列举元素， 并定义一个空字典；
        （2）用目标值target去减列举的元素， 如果它们的差在字典中，则返回它们的下标； 
        （3）如果它们的差不在字典中， 则把该值赋值给空字典， 直到找到符合的值， 否则返回None。
时间复杂度： O(n)
"""
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: 整数数组： nums: List[int]
        :param target: 目标值： target: int
        :return: 返回值： List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6]
    target1 = 9
    s1 = Solution1()
    print(s1.twoSum(nums=nums1, target=target1))



