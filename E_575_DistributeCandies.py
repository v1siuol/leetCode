"""
207 / 207 test cases passed.
Status: Accepted
Runtime: 242 ms
You are here!
Your runtime beats 30.74 % of python submissions.
"""
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        lst = len(candies)
        st = len(set(candies))
        return st if st < lst / 2 else lst // 2
