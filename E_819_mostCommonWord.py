from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 32 ms, faster than 91.31% of Python3 online submissions for Most Common Word.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in banned_set).most_common(1)[0][0]
