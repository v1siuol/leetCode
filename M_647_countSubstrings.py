from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 116 ms, faster than 89.69% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 13.8 MB, less than 37.71% of Python3 online submissions for Palindromic Substrings.
"""

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        n = len(s)
        for center in range(2 * n + 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                ret += 1
                left -= 1
                right += 1
        return ret 

