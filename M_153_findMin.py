"""
Runtime: 28 ms, faster than 99.38% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.4 MB, less than 5.32% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
"""
from __future__ import annotations 


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if right == 0:
            return nums[0]

        if nums[0] < nums[right]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                if nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[0] 




s = Solution()
print(s.findMin([3,4,5,1,2]))  # 1 
print(s.findMin([4,5,6,7,0,1,2]))  # 0 
print(s.findMin([4,5,6,7,0,1,2]))  # 0 

