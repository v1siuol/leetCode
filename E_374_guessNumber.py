"""
Success
Details 
Runtime: 16 ms, faster than 90.22% of Python online submissions for Guess Number Higher or Lower.
Memory Usage: 11.8 MB, less than 37.42% of Python online submissions for Guess Number Higher or Lower.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while l <= r:
            m = (l+r) // 2
            ret = guess(m)
            # print(l, m, r)
            if ret == 0:
                return m
            elif ret == 1:
                l = m + 1
            elif ret == -1:
                r = m - 1

        return 0 

