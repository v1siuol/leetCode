"""
17 / 17 test cases passed.
Status: Accepted
Runtime: 99 ms
You are here!
Your runtime beats 51.08% of python submissions
"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        re = []
        for i in findNums:
            a = nums.index(i) + 1
            while a < len(nums):
                if nums[a] > i:
                    re.append(nums[a])
                    break
                a += 1
            else:
                re.append(-1)
        return re
