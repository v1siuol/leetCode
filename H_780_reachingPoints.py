from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 24 ms, faster than 99.24% of Python3 online submissions for Reaching Points.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Reaching Points.
"""
# 反向日神仙 
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return (sx == tx and sy <= ty and (ty-sy)%sx == 0) or (sy == ty and sx <= tx and (tx-sx)%sy == 0)
