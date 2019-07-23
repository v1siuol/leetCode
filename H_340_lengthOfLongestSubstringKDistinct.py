from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 100 ms, faster than 34.52% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Memory Usage: 14.3 MB, less than 5.39% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # sliding window 
        if k == 0 or s == '':
            return 0
        match_count = 0
        word_count = collections.defaultdict(int)
        res = 0
        start = 0
        min_length = 0
        for i in range(len(s)):
            if word_count.get(s[i], 0) == 0:
                # not in window yet 
                match_count += 1
            word_count[s[i]] += 1

            if match_count > k:
                word_count[s[start]] -= 1
                start += 1
                while word_count[s[start-1]] > 0:
                    word_count[s[start]] -= 1
                    start += 1

                match_count -= 1
            min_length = max(min_length, i-start+1)

        return min_length 

