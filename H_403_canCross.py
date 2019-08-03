from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 256 ms, faster than 49.02% of Python3 online submissions for Frog Jump.
Memory Usage: 15.6 MB, less than 19.23% of Python3 online submissions for Frog Jump.
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        loc_contain_jump = collections.defaultdict(set)
        loc_contain_jump[0] = set([0])
        stone_set = set(stones)

        for stone in stones[:-1]:
            jumps = loc_contain_jump.get(stone, set())
            for k in jumps:
                if k > 1 and stone+k-1 in stone_set:
                    loc_contain_jump[stone+k-1].add(k-1)
                if k > 0 and stone+k in stone_set:
                    loc_contain_jump[stone+k].add(k)
                if stone+k+1 in stone_set:
                    loc_contain_jump[stone+k+1].add(k+1)

        return len(loc_contain_jump.get(stones[-1], set())) > 0



s = Solution()
print(s.canCross([0,1,3,5,6,8,12,17]))
print(s.canCross([0,1,2,3,4,8,9,11]))
