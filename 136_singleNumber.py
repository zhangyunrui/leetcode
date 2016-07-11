# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i < j:
            k = (i + j) / 2
            if isBadVersion(k):
                j = k
            else:
                i = k + 1
        return i

    # def firstBadVersion(self, n):
    #     return bisect.bisect(type('', (), {'__getitem__': lambda self, i: isBadVersion(i)})(), False, 0, n)
    #
    # def firstBadVersion(self, n):
    #     class Wrap:
    #         def __getitem__(self, i):
    #             return isBadVersion(i)
    #
    #     return bisect.bisect(Wrap(), False, 0, n)
