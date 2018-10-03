"""
600 / 600 test cases passed.
Status: Accepted
Runtime: 45 ms
You are here!
Your runtime beats 63.55% of python submissions.
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        return bin(n).count("1")

print(Solution().hammingWeight(11))
print(Solution().hammingWeight(-3))
