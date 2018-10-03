"""
93 / 93 test cases passed.
Status: Accepted
Runtime: 24 ms
You are here! 
Your runtime beats 63.81 % of python submissions.
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        temp = n - 2
        rv = True
        if n < 2:
            return True
        if bits[temp] == 0:
            return True
        else:
            rv = False
        while temp > 0:
            temp -= 1
            if bits[temp] == 0:
                return rv
            else:
                rv = False if rv else True
        return rv
