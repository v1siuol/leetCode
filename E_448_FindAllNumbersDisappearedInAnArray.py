"""
34 / 34 test cases passed.
Status: Accepted
Runtime: 242 ms
You are here!
Your runtime beats 98.68% of python submissions.
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(list(range(1, len(nums)+1))) - set(nums))

print(Solution().findDisappearedNumbers([1,1]))