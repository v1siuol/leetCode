"""
Success
Details 
Runtime: 36 ms, faster than 84.71% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.2 MB, less than 6.04% of Python3 online submissions for Length of Last Word.
"""
class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        # 用len啊 
        if not s:
            return 0
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                break
            i -= 1
        if i < 0:
            return 0
        word_end = i
        i -= 1
        while i >= 0:
            if s[i] == ' ':
                return word_end - i
            i -= 1
        return word_end + 1


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord(""))
print(s.lengthOfLastWord("123"))
print(s.lengthOfLastWord("a"))
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("  "))


