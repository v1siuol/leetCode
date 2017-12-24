"""
204 / 204 test cases passed.
Status: Accepted
Runtime: 69 ms
You are here!
Your runtime beats 25.35 % of python3 submissions.
"""
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        magic_num = 5
        if n in [0, 1, 2]:
            return True
        else:
            while magic_num <= n:
                if magic_num == n:
                    return True
                if magic_num & 1:  # ji
                    magic_num *= 2
                else:
                    magic_num = magic_num * 2 + 1
        return False
