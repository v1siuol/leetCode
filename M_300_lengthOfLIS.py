"""
Success
Details 
Runtime: 40 ms, faster than 88.40% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 13.2 MB, less than 83.98% of Python3 online submissions for Longest Increasing Subsequence.
"""
from __future__ import annotations 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            i = 0
            j = size
            while i < j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid

            tails[i] = num
            size = max(i+1, size)

        return size 






s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4 

