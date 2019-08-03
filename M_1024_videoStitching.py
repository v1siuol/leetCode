from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 40 ms, faster than 84.62% of Python3 online submissions for Video Stitching.
Memory Usage: 13.8 MB, less than 5.15% of Python3 online submissions for Video Stitching.
"""

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        curr_clip = [-1, 0]
        c = 0
        for start, end in sorted(clips):
            if curr_clip[1] >= T:
                return c
            if start > curr_clip[1]:
                return -1
            if curr_clip[0] < start <= curr_clip[1]:
                c += 1
                curr_clip[0] = curr_clip[1]
            curr_clip[1] = max(curr_clip[1], end)

        return c if curr_clip[1] >= T else -1

