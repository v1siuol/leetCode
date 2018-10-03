"""
Author  => v1siuol
Date    => 2018.05.31
276 / 276 test cases passed.
Status: Accepted
Runtime: 56 ms
You are here! 
Your runtime beats 49.04 % of python3 submissions.
"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        best = [0 for i in range(n)]

        best[0] = cost[0]
        best[1] = cost[1]
        i = 2

        while i < n:
            best[i] = min(best[i-1]+cost[i], best[i-2]+cost[i])
            i += 1
        return min(best[n-1], best[n-2])

print(Solution().minCostClimbingStairs([0,1,1,0]))
