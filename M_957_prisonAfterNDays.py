from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 44 ms, faster than 66.25% of Python3 online submissions for Prison Cells After N Days.
Memory Usage: 14 MB, less than 5.23% of Python3 online submissions for Prison Cells After N Days.
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = 14 if N % 14 == 0 else N % 14
        # N -= max(N - 1, 0) // 14 * 14
        for _ in range(N):
            cells = [0] + [cells[i-1]^cells[i+1]^1 for i in range(1,7)] + [0]
        return cells 

        # dict 缩短 正解
