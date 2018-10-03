"""
113 / 113 test cases passed.
Status: Accepted
Runtime: 42 ms
You are here!
Your runtime beats 78.69 % of python submissions.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        res = len(nums)
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
                res -= 1
            else:
                i += 1
        return res

print(Solution().removeElement([3,2,2,3], 3))
