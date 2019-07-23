from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 92 ms, faster than 94.39% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.5 MB, less than 9.26% of Python3 online submissions for Minimum Window Substring.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.defaultdict(int)
        for char in t:
            count_t[char] += 1

        start = 0
        end = 0
        counter = len(t)
        min_start = 0
        min_length = float('inf')

        while end < len(s):
            if count_t[s[end]] > 0:
                counter -= 1
            count_t[s[end]] -= 1
            end += 1
            # small the valid window
            while counter == 0:
                if end - start < min_length:
                    min_start = start
                    min_length = end - start
                count_t[s[start]] += 1
                if count_t[s[start]] > 0:
                    counter += 1
                start += 1

        if min_length != float('inf'):
            return s[min_start:min_start+min_length]
        return ''
