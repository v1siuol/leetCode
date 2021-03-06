from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 76 ms, faster than 55.97% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.4 MB, less than 13.25% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 看了diss 主要有set跟dict两种 
#         # Time: O(n)
#         # Space: O(n)

#         ret = 0
#         used = set()

#         left = 0
#         right = 0

#         while right < len(s):
#             if s[right] in used:
#                 used.remove(s[left])
#                 left += 1
#             else:
#                 used.add(s[right])
#                 ret = max(ret, len(used))
#                 right += 1

#         return ret 



"""
Success
Details 
Runtime: 52 ms, faster than 98.28% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.1 MB, less than 96.64% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 看了diss 主要有set跟dict两种 
#         # Time: O(n)
#         # Space: O(n)
#         ret = 0
#         left = -1
#         dct = dict()

#         for idx, char in enumerate(s):
#             if char in dct:
#                 left = max(left, dct[char])
#             dct[char] = idx
#             ret = max(ret, idx-left)

#         return ret 


"""
Success
Details 
Runtime: 64 ms, faster than 73.91% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ??? 什么农民算法 
        have = set()
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in have:
                have.add(s[i])
                res = max(res, i-start+1)
            else:
                have.remove(s[start])
                start += 1
                while s[i] in have:
                    have.remove(s[start])
                    start += 1
                have.add(s[i])
        return res
    