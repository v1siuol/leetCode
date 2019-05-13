"""
Success
Details 
Runtime: 56 ms, faster than 15.24% of Python3 online submissions for Implement strStr().
Memory Usage: 13.3 MB, less than 5.13% of Python3 online submissions for Implement strStr().
"""
class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        h_i = 0

        while True:
            n_i = 0
            while True:
                if n_i == len(needle):
                    return h_i
                if h_i + n_i == len(haystack):
                    return -1
                if needle[n_i] != haystack[h_i+n_i]:
                    break
                n_i += 1
            h_i += 1

        return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("ababaa", "abaa"))
