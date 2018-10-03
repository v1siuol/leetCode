"""
1101 / 1101 test cases passed.
Status: Accepted
Runtime: 52 ms
You are here!
Your runtime beats 46.13% of python submissions.
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        re = sum(map(int, list(str(num))))
        while re >= 10:
            re = sum(map(int, list(str(re))))
        return re

print(Solution().addDigits(38))