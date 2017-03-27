"""
95 / 95 test cases passed.
Status: Accepted
Runtime: 52 ms
You are here!
Your runtime beats 66.83% of python submissions.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        re = 0
        hasNoOdd = True
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        for j in dct.values():
            if j & 1 == 0:  # even
                re += j
            elif hasNoOdd:
                re += j
                hasNoOdd = False
            else:
                re += (j-1)
        return re
