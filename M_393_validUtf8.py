from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 128 ms, faster than 67.47% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 14.1 MB, less than 28.00% of Python3 online submissions for UTF-8 Validation.
"""

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for char in data:
            if count == 0:
                if char >> 3 == 0b11110:
                    count = 3
                elif char >> 4 == 0b1110:
                    count = 2
                elif char >> 5 == 0b110:
                    count = 1
                elif char >> 7 == 0b1:
                    return False
            else:
                if char >> 6 == 0b10:
                    count -= 1
                else:
                    return False
        return count == 0
    

