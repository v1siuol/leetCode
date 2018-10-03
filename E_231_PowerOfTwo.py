"""
1108 / 1108 test cases passed.
Status: Accepted
Runtime: 52 ms
You are here!
Your runtime beats 49.18% of python submissions.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #print(bin(n))
        return bin(n).count("1") == 1 if n > 0 else False

print(Solution().isPowerOfTwo(8))
print(Solution().isPowerOfTwo(-16))
