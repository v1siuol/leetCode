"""
18 / 18 test cases passed.
Status: Accepted
Runtime: 72 ms
You are here!
Your runtime beats 35.36% of python submissions.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

print(Solution().containsDuplicate([1,1,2]))
print(Solution().containsDuplicate([1,2]))
