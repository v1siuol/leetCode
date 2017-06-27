"""
30 / 30 test cases passed.
Status: Accepted
Runtime: 106 ms
You are here!
Your runtime beats 31.65 % of python submissions.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        re = ""
        for i in s.split():
            re += i[::-1] + " "
        return re[:-1]

print(Solution().reverseWords("Let's take LeetCode contest"))

