"""
Success
Details 
Runtime: 40 ms, faster than 96.71% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 13.2 MB, less than 17.97% of Python3 online submissions for Isomorphic Strings.
"""
class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        # Note: You may assume both s and t have the same length.
        s2t = dict()
        used = set()
        for idx in range(len(s)):
            if s[idx] not in s2t:
                if t[idx] in used:
                    return False
                s2t[s[idx]] = t[idx]
                used.add(t[idx])
            else:
                if s2t[s[idx]] != t[idx]:
                    return False
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("ab", "aa"))


