"""
62 / 62 test cases passed.
Status: Accepted
Runtime: 145 ms
You are here!
Your runtime beats 12.15 % of python3 submissions.
"""
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        r, l, u, d = 0, 0, 0, 0
        for i in range(len(moves)):
            if 'R' == moves[i]:
                r += 1
            elif 'L' == moves[i]:
                l += 1
            elif 'U' == moves[i]:
                u += 1
            elif 'D' == moves[i]:
                d += 1
        return r == l and u == d
