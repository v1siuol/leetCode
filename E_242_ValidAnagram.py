"""
34 / 34 test cases passed.
Status: Accepted
Runtime: 185 ms
You are here!
Your runtime beats 3.88% of python submissions.
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        di = dict()
        for i in s:
            if i not in di.keys():
                di[i] = 1
            else:
                di[i] += 1
        for i in t:
            if i not in di:
                return False
            elif di[i] == 0:
                return False
            else:
                di[i] -= 1
        return sum(di.values()) == 0
