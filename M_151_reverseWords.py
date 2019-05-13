"""
Success
Details 
Runtime: 36 ms, faster than 98.80% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Reverse Words in a String.
"""
class Solution:
    def reverseWords(self, s: 'str') -> 'str':
        return ' '.join(s.split()[::-1])



s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world!  "))
print(s.reverseWords("a good   example"))
