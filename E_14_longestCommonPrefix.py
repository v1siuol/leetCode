"""
Success
Details 
Runtime: 36 ms, faster than 97.43% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.3 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
"""
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ''
        i = 0
        is_on = True
        while is_on and i < len(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    is_on = False
                    i -= 1
                    break
            i += 1

        return strs[0][:i]


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["","racecar","car"]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(['']))
print(s.longestCommonPrefix(['', '']))
print(s.longestCommonPrefix(['a']))
