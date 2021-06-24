from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 36 ms, faster than 95.15% of Python3 online submissions for Partition Labels.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Partition Labels.
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        res = []
        anchor = j = 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                res.append(i-anchor+1)
                anchor = i + 1  # start at next char
        return res
