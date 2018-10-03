"""
84 / 84 test cases passed.
Status: Accepted
Runtime: 199 ms
You are here!
Your runtime beats 3.47% of python submissions.
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        c = 0
        while min(nums) != max(nums):
            nums.sort()
            for i in range(len(nums)-1):
                nums[i] += 1
            c += 1
        return c
        """
        re = 0
        nums.sort()
        for i in range(1,len(nums)):
            re += nums[i] - nums[0]
        return re
print(Solution().minMoves([1,999999]))
