"""
Success
Details 
Runtime: 32 ms, faster than 98.45% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 13.4 MB, less than 55.39% of Python3 online submissions for Search in Rotated Sorted Array II.
"""
from __future__ import annotations 


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True 

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:
                # first half in order
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # second half in order 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1

        return False



s = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))  # True 


nums = [4,5,6,7,0,1,2]
target = 3
print(s.search(nums, target))  # False


nums = [2,5,6,0,0,1,2]
target = 0
print(s.search(nums, target))  # True

nums = [2,5,6,0,0,1,2]
target = 3
print(s.search(nums, target))  # False

