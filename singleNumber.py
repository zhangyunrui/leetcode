# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if not i:
                x = nums[i]
            y = x ^ nums[i + 1]

            print i, x, nums[i + 1], y

            x = y

            # return reduce(lambda x, y: x ^ y, nums)


print Solution().singleNumber([1, 9, 1])
