"""
121 / 121 test cases passed.
Status: Accepted
Runtime: 59 ms
You are here!
Your runtime beats 59.96% of python submissions.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(range(1, len(nums)+1))) - sum(nums)
        
