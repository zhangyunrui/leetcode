# -*- coding: utf-8 -*-
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        L = [''] * numRows
        if numRows == 1 or numRows >= len(s):
            return s
        index, step = 0, 1
        for x in s:
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            L[index] += x
            index += step
        return ''.join(L)


print Solution().convert('abcde', 4)
