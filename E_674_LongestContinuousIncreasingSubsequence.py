"""
Author  => v1siuol
Date    => 2018.05.31
36 / 36 test cases passed.
Status: Accepted
Runtime: 44 ms
You are here! 
Your runtime beats 98.30 % of python3 submissions.
"""
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        templ = 1
        maxre = 0
        i = 1
        n = len(nums)
        if n == 0:
            return 0
        while i < n:
            if nums[i] > nums[i-1]:
                templ += 1
            else:
                if maxre < templ:
                    maxre = templ
                templ = 1
            i += 1
        if maxre < templ:
            maxre = templ

        return maxre
