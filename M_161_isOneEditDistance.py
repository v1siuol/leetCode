"""
Success
Details 
Runtime: 28 ms, faster than 100.00% of Python3 online submissions for One Edit Distance.
Memory Usage: 13.2 MB, less than 5.05% of Python3 online submissions for One Edit Distance.
"""

class Solution:
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) < len(t):
                    return s[i:] == t[i+1:]
                elif len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return abs(len(s)-len(t)) == 1  # all same except the last char 


s = Solution()
print(s.isOneEditDistance("ab", "acb"))
print(s.isOneEditDistance("cad", "ad"))
print(s.isOneEditDistance("cab", "ad"))
print(s.isOneEditDistance("1203", "1213"))
print(s.isOneEditDistance("a", ""))
print(s.isOneEditDistance("", ""))
