# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return not (n % 4 == 0)
        return bool(n & 3)


print Solution().canWinNim(8)
