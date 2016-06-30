# -*- coding: utf-8 -*-
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        outStr = [''] * numRows
        a = 0
        x = 1
        for S in s:
            if a < 1:
                x = 1
            elif a > numRows - 2:
                x = -1
            outStr[a] += S
            a += x
        return ''.join(outStr)

print Solution().convert('123456789', 5)
