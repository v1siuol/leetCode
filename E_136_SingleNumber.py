"""
15 / 15 test cases passed.
Status: Accepted
Runtime: 66 ms
You are here!
Your runtime beats 28.32% of python submissions.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i != len(nums) - 1:
            if nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 1
            i += 1
        return nums[-1]

print(Solution().singleNumber([1,1,2,3,3]))
