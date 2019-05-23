"""
Success
Details 
Runtime: 40 ms, faster than 92.99% of Python3 online submissions for Paint House.
Memory Usage: 13.1 MB, less than 73.88% of Python3 online submissions for Paint House.
"""

class Solution:
    def minCost(self, costs: 'List[List[int]]') -> 'int':
        # 可以优化空间 
        n = len(costs)

        dp = [[None, None, None] for _ in range(n)]
        if n <= 0:
            return 0
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]


        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

        return min(dp[n-1])




S = Solution()
print(S.minCost([[17,2,17],[16,16,5],[14,3,19]]))
