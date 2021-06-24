from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 32 ms, faster than 98.07% of Python3 online submissions for Before and After Puzzle.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Before and After Puzzle.
"""
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        first = collections.defaultdict(set)
        last = collections.defaultdict(set)
        ret = set()

        for p in phrases:
            strs = p.split()
            p_last = p[len(strs[0]):]  # include leading space 

            if strs[0] in last:
                ret |= {s1 + p_last for s1 in last[strs[0]]}

            if strs[-1] in first:
                ret |= {p + s2 for s2 in first[strs[-1]]}

            first[strs[0]].add(p_last)
            last[strs[-1]].add(p)

        return sorted(ret)
