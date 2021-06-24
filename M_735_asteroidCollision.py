from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 100 ms, faster than 91.88% of Python3 online submissions for Asteroid Collision.
Memory Usage: 13.9 MB, less than 50.00% of Python3 online submissions for Asteroid Collision.
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []
        for new in asteroids:
            while ret and new < 0 < ret[-1]:
                if ret[-1] < -new:
                    ret.pop()
                    continue
                elif ret[-1] == -new:
                    ret.pop()
                break
            else:
                ret.append(new)
        return ret 
