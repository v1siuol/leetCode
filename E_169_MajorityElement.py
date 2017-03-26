"""
44 / 44 test cases passed.
Status: Accepted
Runtime: 59 ms
You are here!
Your runtime beats 82.26% of python submissions.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]
        
