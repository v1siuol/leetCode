"""
476 / 476 test cases passed.
Status: Accepted
Runtime: 78 ms
You are here!
Your runtime beats 15.26% of python submissions.
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        result.reverse()
        return "".join(result)
print(Solution().reverseString("hello"))