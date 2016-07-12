import copy
import operator


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # for i, num in enumerate(nums):
        #     _nums = copy.deepcopy(nums)
        #     _nums.pop(i)
        #     try:
        #         _nums.index(num)
        #     except ValueError:
        #         return num

        # for i in list(set(nums)):
        #     try:
        #         nums.pop(nums.index(i))
        #         nums.pop(nums.index(i))
        #     except ValueError:
        #         return i

        return reduce(lambda x, y: x ^ y, nums)

    # def singleNumber1(self, nums):
    #     dic = {}
    #     for num in nums:
    #         dic[num] = dic.get(num, 0)+1
    #     for key, val in dic.items():
    #         if val == 1:
    #             return key
    #
    # def singleNumber2(self, nums):
    #     res = 0
    #     for num in nums:
    #         res ^= num
    #     return res
    #
    # def singleNumber3(self, nums):
    #     return 2*sum(set(nums))-sum(nums)
    #
    # def singleNumber4(self, nums):
    #     return reduce(lambda x, y: x ^ y, nums)
    #
    # def singleNumber(self, nums):
    #     return reduce(operator.xor, nums)

print Solution().singleNumber([1, 0, 1])
