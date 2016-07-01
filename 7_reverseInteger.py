# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if - 0x7fffffff - 1 < x < 0x7fffffff:
            rvt = 0
            sign = -1 if x < 0 else 1
            x = abs(x)
            while x > 0:
                rvt = rvt * 10 + x % 10
                x /= 10
            rvt = rvt * sign
            if - 0x7fffffff - 1 < rvt < 0x7fffffff:
                return rvt
        return 0



