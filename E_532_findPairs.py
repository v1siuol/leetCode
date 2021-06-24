from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 136 ms, faster than 92.85% of Python3 online submissions for K-diff Pairs in an Array.
Memory Usage: 14.3 MB, less than 96.77% of Python3 online submissions for K-diff Pairs in an Array.
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_counter = collections.defaultdict(int)

        for n in nums:
            num_counter[n] += 1

        counter = 0
        if k < 0:
            return 0
        elif k == 0:
            for c in num_counter.values():
                if c >= 2:
                    counter += 1
        else:
            for n in num_counter.keys():
                # one way no dupl
                if num_counter.get(n+k, 0) > 0:
                    counter += 1

        return counter
