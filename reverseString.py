# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        return ''.join(reversed(s))

print Solution().reverseString('hello')