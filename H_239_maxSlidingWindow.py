from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 180 ms, faster than 71.05% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 20 MB, less than 15.38% of Python3 online submissions for Sliding Window Maximum.
"""

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) == 0:
#             return []
#         if k == 0:
#             return []

#         res = []
#         deque = collections.deque()
#         for idx in range(len(nums)):

#             while deque and deque[0] < idx - k + 1:
#                 # out of bound 
#                 deque.popleft()

#             while deque and nums[deque[-1]] <= nums[idx]:
#                 # get rid of smaller 
#                 deque.pop()

#             deque.append(idx)
#             if idx >= k-1:
#                 res.append(nums[deque[0]])

#         return res


"""
Success
Details 
Runtime: 152 ms, faster than 99.17% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 19.4 MB, less than 88.46% of Python3 online submissions for Sliding Window Maximum.
"""
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         # O(n)-O(n^2) O(n)
#         if len(nums) < k or k == 0:
#             return []
#         curr_max = nums[0]
#         curr_max_idx = 0
#         ret = []
        
#         for i in range(len(nums)):
#             if nums[i] >= curr_max:
#                 curr_max = nums[i]
#                 curr_max_idx = i
#             else:
#                 if curr_max_idx <= i-k:
#                     curr_max = nums[i-k+1]
#                     curr_max_idx = i-k+1
#                     for j in range(i-k+2, i+1):
#                         if nums[j] >= curr_max:
#                             curr_max = nums[j]
#                             curr_max_idx = j
                            
#             if i >= k-1:
#                 ret.append(curr_max)
                
#         return ret 


"""
Success
Details 
Runtime: 168 ms, faster than 91.17% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 19.5 MB, less than 88.46% of Python3 online submissions for Sliding Window Maximum.
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n) O(n)
        queue = collections.deque()  # idx
        ret = []
        for idx, num in enumerate(nums):

            # pop old
            if queue and queue[0] <= idx-k:
                queue.popleft()

            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(idx)

            if idx >= k-1:
                ret.append(nums[queue[0]])

        return ret
