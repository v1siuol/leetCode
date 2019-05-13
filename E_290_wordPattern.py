"""
Success
Details 
Runtime: 32 ms, faster than 99.17% of Python3 online submissions for Word Pattern.
Memory Usage: 13 MB, less than 5.47% of Python3 online submissions for Word Pattern.
"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        m1 = dict()
        m2 = dict()
        i = 0
        j = 0
        lst = str.split()
        unique = 0
        while i < len(pattern) and j < len(lst):
            if pattern[i] not in m1:
                m1[pattern[i]] = unique
            if lst[j] not in m2:
                m2[lst[j]] = unique

            if m1[pattern[i]] != m2[lst[j]]:
                return False

            unique += 1
            i += 1
            j += 1
        return i == len(pattern) and j == len(lst)




s = Solution()
pattern = "abba"
str = "dog cat cat dog"
print(s.wordPattern(pattern, str))

pattern = "abba"
str = "dog cat cat fish"
print(s.wordPattern(pattern, str))

pattern = "aaaa"
str = "dog cat cat dog"
print(s.wordPattern(pattern, str))

pattern = "abba"
str = "dog dog dog dog"
print(s.wordPattern(pattern, str))

pattern = "abb"
str = "dog dog dog dog"
print(s.wordPattern(pattern, str))

pattern = ""
str = ""
print(s.wordPattern(pattern, str))

pattern = ""
str = "1"
print(s.wordPattern(pattern, str))
