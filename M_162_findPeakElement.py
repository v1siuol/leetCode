"""
Success
Details 
Runtime: 36 ms, faster than 86.63% of Python3 online submissions for Find Peak Element.
Memory Usage: 13.2 MB, less than 65.87% of Python3 online submissions for Find Peak Element.
"""
from __future__ import annotations 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 变形 
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left




s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
