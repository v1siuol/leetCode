"""
Author  => v1siuol
Date    => 2018.05.13
113 / 113 test cases passed.
Status: Accepted
Runtime: 36 ms
You are here! 
Your runtime beats 99.62 % of python3 submissions.
"""
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c_a = False
        c_l = 0

        for i in s:

            if i == 'L':
                if c_l >= 2:
                    return False
                c_l += 1
            else:
                c_l = 0
                if i == 'A':
                    if c_a:
                        return False
                    c_a = True

        return True

            