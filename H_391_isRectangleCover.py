from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 388 ms, faster than 89.97% of Python3 online submissions for Perfect Rectangle.
Memory Usage: 19.7 MB, less than 50.00% of Python3 online submissions for Perfect Rectangle.
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        area = 0
        corners = set()

        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            area += (x2 - x1) * (y2 - y1)

            top_left = (x1, y2)
            top_right = (x2, y2)
            bot_left = (x1, y1)
            bot_right = (x2, y1)

            # dupl 
            for c in [top_left, top_right, bot_left, bot_right]:
                if c in corners:
                    corners.remove(c)
                else:
                    corners.add(c)

        # corners check
        top_left = (min_x, max_y)
        top_right = (max_x, max_y)
        bot_left = (min_x, min_y)
        bot_right = (max_x, min_y)
        if any(c not in corners for c in [top_left, top_right, bot_left, bot_right]) or len(corners) != 4:
            return False

        # center empty 
        return area == (max_x-min_x) * (max_y-min_y)
