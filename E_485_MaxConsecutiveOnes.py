"""
41 / 41 test cases passed.
Status: Accepted
Runtime: 95 ms
You are here!
Your runtime beats 64.57% of python submissions.
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        temp = 0
        for num in nums:
            if num == 1:
                result += 1
                if result > temp:
                    temp = result
            else:
                result = 0
        return temp
