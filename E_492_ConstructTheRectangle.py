"""
50 / 50 test cases passed.
Status: Accepted
Runtime: 2729 ms
You are here!
Your runtime beats 0.54% of python submissions.
"""
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = l = int(area ** 0.5)
        while l * w != area:
            l += 1
            w = area // l
        return[l, w]
