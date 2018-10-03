"""
位运算
260 / 260 test cases passed.
Status: Accepted
Runtime: 20 ms
You are here! 
Your runtime beats 100.00 % of python submissions.
"""
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        curr_gap, max_gap = 0, 0

        # get rid of tail 0s
        while N > 0:
            if N & 1 == 0:
                N = N >> 1
            else: 
                break

        while N > 0:
            if N & 1 == 1:
                if curr_gap > max_gap:
                    max_gap = curr_gap
                curr_gap = 1
            else:
                curr_gap += 1
            N = N >> 1

        return max_gap if max_gap != 0 else 0

print(Solution().binaryGap(22))
print(Solution().binaryGap(5))
print(Solution().binaryGap(6))
print(Solution().binaryGap(8))