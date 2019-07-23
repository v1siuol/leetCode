from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 100 ms, faster than 96.51% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15 MB, less than 5.39% of Python3 online submissions for Find All Anagrams in a String.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        ret = []
        char_count = dict()
        for char in p:
            char_count[char] = char_count.get(char, 0) + 1
        count = len(char_count)

        for i in range(len(s)):
            if s[i] in char_count:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    count -= 1

            while count == 0:
                if s[start] in char_count:
                    char_count[s[start]] += 1
                    if char_count[s[start]] > 0:
                        count += 1
                if i+1 - start == len(p):
                    ret.append(start)
                start += 1
        return ret 
