"""
83 / 83 test cases passed.
Status: Accepted
Runtime: 132 ms
You are here!
Your runtime beats 33.52 % of python submissions.
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        #print(nums)

        if nums[0] < 0 and nums[1] < 0 and nums[-2] * nums[-3] * nums[-1] < nums[0] * nums[1] * nums[-1]:
            return nums[0] * nums[1] * nums[-1]
        else:
            return nums[-1] * nums[-2] * nums[-3]

#print(Solution().maximumProduct([1, 2, 3, 4]))

print(Solution().maximumProduct([-4,-3,-2,-1,60]))
print(Solution().maximumProduct([-4,-3,-2,-1,-60]))