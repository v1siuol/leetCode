"""
21 / 21 test cases passed.
Status: Accepted
Runtime: 95 ms
You are here!
Your runtime beats 68.75% of python submissions.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        c = 0
        re = 0
        while i < len(s):
            if s[i] >= g[c]:
                re += 1
                c += 1
                if c >= len(g):
                    return re
            i += 1
        return re


print(Solution().findContentChildren([1,2,3], [1,1]))
print(Solution().findContentChildren([1,2], [1,2,3]))
