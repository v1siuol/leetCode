from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 52 ms, faster than 19.48% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 13.8 MB, less than 5.51% of Python3 online submissions for Top K Frequent Words.
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # counter + heap 
        counter = collections.Counter(words)
        max_heap = [(-cnt, word) for word, cnt in counter.items()]
        heapq.heapify(max_heap)
        res = []
        for _ in range(k):
            cnt, word = heapq.heappop(max_heap)
            res.append(word)
        return res 
