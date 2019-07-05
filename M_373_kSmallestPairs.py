"""
Success
Details 
Runtime: 56 ms, faster than 95.48% of Python3 online submissions for Find K Pairs with Smallest Sums.
Memory Usage: 13.6 MB, less than 48.26% of Python3 online submissions for Find K Pairs with Smallest Sums.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)
        res = []
        if not nums1 or not nums2 or k == 0:
            return res 
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
        while k > 0 and min_heap:
            k -= 1
            curr = heapq.heappop(min_heap)
            res.append((curr[1], curr[2]))
            if curr[3] < len(nums2) - 1:
                heapq.heappush(min_heap, (curr[1]+nums2[curr[3]+1], curr[1], nums2[curr[3]+1], curr[3]+1))
        return res 



s = Solution()


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(s.kSmallestPairs(nums1, nums2, k)) 

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(s.kSmallestPairs(nums1, nums2, k)) 

nums1 = [1,2]
nums2 = [3]
k = 3
print(s.kSmallestPairs(nums1, nums2, k)) 

nums1 = [3,5,7,9]
nums2 = []
k = 1
print(s.kSmallestPairs(nums1, nums2, k)) 

