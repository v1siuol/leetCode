from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 776 ms, faster than 81.78% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.4 MB, less than 87.35% of Python3 online submissions for Longest Palindromic Substring.
"""

"""
目前 O(n^2) 长度处理迷了 
最优 O(n) Manacher's algorithm 
"""

# class Solution:
#     def longestPalindrome(self, s: 'str') -> 'str':

#         def bi_expand(left, right):
#             ret_length = 0
#             while left >= 0 and right < n and s[left] == s[right]:
#                 ret_length = right - left

#                 left -= 1
#                 right += 1
#             return ret_length

#         n = len(s)
#         max_length = -1
#         ret_str = ''
#         for i in range(n):
#             length_with_center = bi_expand(i, i)  # more on 2
#             length_without_center = bi_expand(i, i+1)  # more on 1  

#             # print(i, length_with_center, length_without_center, max_length)

#             if length_with_center > max_length:
#                 max_length = length_with_center
#                 ret_str = s[i-length_with_center//2:i+length_with_center//2+1]

#             if length_without_center > max_length:
#                 max_length = length_without_center
#                 ret_str = s[i-length_without_center//2:i+length_without_center//2+2]

#         return ret_str


"""
Success
Details 
Runtime: 932 ms, faster than 69.97% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.2 MB, less than 57.45% of Python3 online submissions for Longest Palindromic Substring.
"""

# class Solution:
#     def longestPalindrome(self, s: 'str') -> 'str':
#         def bi_expand(left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return right - left - 1

#         if len(s) == 0:
#             return ''

#         start = 0
#         end = 0
#         for i in range(len(s)):
#             with_center = bi_expand(i, i)
#             without_center = bi_expand(i, i+1)

#             l = max(with_center, without_center)

#             if l > end-start+1:
#                 # update
#                 start = i - (l-1) // 2 
#                 end = i + l // 2 

#         return s[start:end+1]



# sol = Solution()
# print(sol.longestPalindrome('babad'))
# print(sol.longestPalindrome('cbbd'))
# print(sol.longestPalindrome(''))
# print(sol.longestPalindrome('a'))
# print(sol.longestPalindrome('ac'))
# print(sol.longestPalindrome('tattarrattat'))


"""
Success
Details 
Runtime: 80 ms, faster than 97.33% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 20.17% of Python3 online submissions for Longest Palindromic Substring.
"""

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # O(n)
#         T = '#'.join('^{}$'.format(s))
#         n = len(T)
#         P = [0] * n
#         C = R = 0

#         for i in range (1, n-1):
#             P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
#             # Attempt to expand palindrome centered at i
#             while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
#                 P[i] += 1
    
#             # If palindrome centered at i expand past R,
#             # adjust center based on expanded palindrome.
#             if i + P[i] > R:
#                 C, R = i, i + P[i]
    
#         # Find the maximum element in P.
#         maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
#         return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


"""
Success
Details 
Runtime: 944 ms, faster than 79.03% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''

        for c in range(len(s)):
            if c != len(s) - 1:
                i, j = expand_from_center(s, c, c)
                if j-i-1 > len(p):
                    p = s[i+1:j]
                i, j = expand_from_center(s, c, c+1)
                if j-i-1 > len(p):
                    p = s[i+1:j]
            else:
                i, j = expand_from_center(s, c, c)
                if j-i-1 > len(p):
                    p = s[i+1:j]

        return p

def expand_from_center(s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return i, j
