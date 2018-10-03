"""
缓存差值字典
29 / 29 test cases passed.
Status: Accepted
Runtime: 32 ms
You are here! 
Your runtime beats 57.58 % of python submissions.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        gap_dict = {}
        for index, num in enumerate(nums):
            if num not in gap_dict:
                gap_dict[target-num] = index  # gap as key, curr_index as value, holding for lookup
            else:
                return [gap_dict[num], index]

print(Solution().twoSum())
