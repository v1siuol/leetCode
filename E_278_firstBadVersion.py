"""
Success
Details 
Runtime: 28 ms, faster than 99.34% of Python3 online submissions for First Bad Version.
Memory Usage: 13.2 MB, less than 27.56% of Python3 online submissions for First Bad Version.
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
