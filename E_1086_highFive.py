from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 60 ms, faster than 99.88% of Python3 online submissions for High Five.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for High Five.
"""
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # dict + minheap
        scores = collections.defaultdict(list)
        for sid, score in items:
            if len(scores[sid]) >= 5:
                heapq.heappushpop(scores[sid], score)
            else:
                heapq.heappush(scores[sid], score)

        return [ [sid, sum(score)//5] for sid, score in scores.items() ]
