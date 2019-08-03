from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 81.19% of Python3 online submissions for Text Justification.
Memory Usage: 13.8 MB, less than 6.03% of Python3 online submissions for Text Justification.
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        count = 0
        curr = []
        for word in words:
            if count + len(curr) + len(word) > maxWidth:
                # overflow 
                for i in range(maxWidth-count):
                    curr[i % (len(curr)-1 or 1)] += ' '
                res.append(''.join(curr))
                count = 0
                curr = []
            curr += [word]
            count += len(word)
        return res + [' '.join(curr).ljust(maxWidth)]
