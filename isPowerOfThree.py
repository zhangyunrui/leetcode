# -*- coding: utf-8 -*-
from math import log


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and abs(log(n, 3) - round(log(n, 3))) <= 1e-10
