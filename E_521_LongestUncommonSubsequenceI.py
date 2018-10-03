"""
41 / 41 test cases passed.
Status: Accepted
Runtime: 39 ms
You are here!
Your runtime beats 64.46 % of python submissions.
"""
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a != b:
            return max(len(a), len(b))
        else:
            return -1

print(Solution().findLUSlength("aba", "cdc"))
