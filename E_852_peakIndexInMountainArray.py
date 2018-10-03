"""
32 / 32 test cases passed.
Status: Accepted
Runtime: 28 ms
You are here! 
Your runtime beats 27.64 % of python submissions.
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
