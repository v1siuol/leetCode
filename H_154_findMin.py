"""
Success
Details 
Runtime: 36 ms, faster than 89.31% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 13.6 MB, less than 16.75% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
"""
from __future__ import annotations 


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 懂 ? 
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                left += 1
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]



s = Solution()
print(s.findMin([3,4,5,1,2]))  # 1 
print(s.findMin([4,5,6,7,0,1,2]))  # 0 
print(s.findMin([4,5,6,7,0,1,2]))  # 0 

print(s.findMin([1,3,5]))  # 1 
print(s.findMin([2,2,2,0,1]))  # 0 


print(s.findMin([10,1,10,10,10]))  # 1 
print(s.findMin([3,1,1,1,1]))  # 1 
