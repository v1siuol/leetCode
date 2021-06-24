from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 28 ms, faster than 96.75% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Robot Bounded In Circle.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for instruction in instructions:
            if instruction == 'G':
                x += dx
                y += dy
            elif instruction == 'L':
                dx, dy = -dy, dx
            elif instruction == 'R':
                dx, dy = dy, -dx
        return x == 0 and y == 0 or dx != 0 or dy != 1
