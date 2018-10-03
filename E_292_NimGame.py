"""
60 / 60 test cases passed.
Status: Accepted
Runtime: 35 ms
You are here!
Your runtime beats 91.69% of python submissions.
"""
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

print(Solution().canWinNim())
# 4 d beishu
