from __future__ import annotations 
import collections 
import random 
import heapq

"""
Success
Details 
Runtime: 44 ms, faster than 62.18% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14 MB, less than 15.31% of Python3 online submissions for Kth Largest Element in an Array.
"""
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         def partition(left, right, pivot_index):
#             pivot = nums[pivot_index]
#             # 1. move pivot to end
#             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
#             # 2. move all smaller elements to the left
#             store_index = left
#             for i in range(left, right):
#                 if nums[i] < pivot:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1

#             # 3. move pivot to its final place
#             nums[right], nums[store_index] = nums[store_index], nums[right]

#             return store_index

#         def select(left, right, k_smallest):
#             if left == right:
#                 return nums[left]
#             pivot_index = random.randint(left, right)
#             pivot_index = partition(left, right, pivot_index)

#             if k_smallest == pivot_index:
#                 return nums[k_smallest]
#             elif k_smallest < pivot_index:
#                 return select(left, pivot_index-1, k_smallest)
#             else:
#                 return select(pivot_index+1, right, k_smallest)

#         return select(0, len(nums)-1, len(nums)-k)


# s = Solution()


# print(s.findKthLargest([3,2,1,5,6,4], 2))  # 5
# print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 4


"""
Success
Details 
Runtime: 56 ms, faster than 97.66% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Kth Largest Element in an Array.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        capacity = 0
        for num in nums:
            heapq.heappush(min_heap, num)
            capacity += 1

            if capacity > k:
                heapq.heappop(min_heap)

        return min_heap[0]
