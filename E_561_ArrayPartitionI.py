"""
81 / 81 test cases passed.
Status: Accepted
Runtime: 156 ms
You are here!
Your runtime beats 29.85 % of python submissions.
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
