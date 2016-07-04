# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: 1 if x == 0 else 0)
        return nums

print Solution().moveZeroes([1,5,3,0,9,0])