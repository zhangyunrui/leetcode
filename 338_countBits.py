# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bin_1s_list = list()

        for n in xrange(num + 1):
            count = 0
            while n:
                count += n % 2
                n /= 2
            bin_1s_list.append(count)

        return bin_1s_list


print Solution().countBits(5)
