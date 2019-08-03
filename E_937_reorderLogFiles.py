from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 48 ms, faster than 30.92% of Python3 online submissions for Reorder Log Files.
Memory Usage: 13.8 MB, less than 6.08% of Python3 online submissions for Reorder Log Files.
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            identity, *content = log.split(maxsplit=1)
            if ord('0') <= ord(content[0][0]) <= ord('9'):
                digits.append(log)
            else:
                heapq.heappush(letters, (content[0],identity,log))

        ret = []
        while letters:
            _, _, log = heapq.heappop(letters)
            ret.append(log)

        return ret + digits

# diy sort by key ok 
