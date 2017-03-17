"""
Submission Details
54 / 54 test cases passed.
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = list(t)
        for i in s:
            l.remove(i)
        return l[0]
