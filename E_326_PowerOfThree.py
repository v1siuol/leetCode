"""
21038 / 21038 test cases passed.
Status: Accepted
Runtime: 228 ms
You are here!
Your runtime beats 45.60% of python submissions.
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #1 3 9 27 81 243
        #if n < 3:
        #    return True if n == 1 else False
        #return self.isPowerOfThree(float(n/3))

        return n > 0 and (1162261467 % n == 0)
