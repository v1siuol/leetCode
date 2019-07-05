"""
Success
Details 
Runtime: 48 ms, faster than 82.17% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 15.8 MB, less than 74.19% of Python3 online submissions for Top K Frequent Elements.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1 
        freq_lst = [(-val, key) for key, val in freq.items()]
        heapq.heapify(freq_lst)
        return [heapq.heappop(freq_lst)[1] for _ in range(k)]


s = Solution()

print(s.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(s.topKFrequent([1], 1))  # [1]
