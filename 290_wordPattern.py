# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution(object):
    # def wordPattern(self, pattern, str):
    #     """
    #     :type pattern: str
    #     :type str: str
    #     :rtype: bool
    #     """
    #     str_list = str.split(' ')
    #     if len(pattern) != len(str_list):
    #         return False
    #
    #     match_dict_p = defaultdict(set)
    #     for i, p in enumerate(pattern):
    #         match_dict_p[p].add(str_list[i])
    #     for vp in match_dict_p.itervalues():
    #         if len(vp) != 1:
    #             return False
    #
    #     match_dict_s = defaultdict(set)
    #     for i, s in enumerate(str_list):
    #         match_dict_s[s].add(pattern[i])
    #     for vs in match_dict_s.itervalues():
    #         if len(vs) != 1:
    #             return False
    #     return True

    # def wordPattern(self, pattern, str):
    #     """
    #     :type pattern: str
    #     :type str: str
    #     :rtype: bool
    #     """
    #     p = pattern
    #     s = str.split()
    #     return map(p.find, p) == map(s.index, s)

    # def wordPattern(self, pattern, str):
    #     """
    #     :type pattern: str
    #     :type str: str
    #     :rtype: bool
    #     """
    #     f = lambda s: map({}.setdefault, s, range(len(s)))
    #     return f(pattern) == f(str.split())

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = pattern
        s = str.split()
        return len(set(zip(p, s))) == len(set(p)) == len(set(s)) and len(p) == len(s)


print Solution().wordPattern('aggg', "dog cat cat cat")
