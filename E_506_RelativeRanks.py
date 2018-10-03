"""
17 / 17 test cases passed.
Status: Accepted
Runtime: 546 ms
You are here!
Your runtime beats 13.85% of python submissions.
"""
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        model = nums[:]
        nums.sort(reverse=True)
        re = []
        for i in model:
            v = nums.index(i)
            if v == 0:
                v = "Gold Medal"
            elif v == 1:
                v = "Silver Medal"
            elif v == 2:
                v = "Bronze Medal"
            else:
                v = str(v+1)
            re.append(v)
        return re

print(Solution().findRelativeRanks([5,4,3,2,1]))