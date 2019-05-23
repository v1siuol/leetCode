"""
Success
Details 
Runtime: 68 ms, faster than 55.56% of Python3 online submissions for Paint House II.
Memory Usage: 13.2 MB, less than 47.22% of Python3 online submissions for Paint House II.
"""
class Solution:
    def minCostII(self, costs: 'List[List[int]]') -> 'int':
        # diss min1 min2没看懂 
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        dp = [costs[0][i] for i in range(k)]
        for j in range(1, n):
            dp = [min(dp[:i]+dp[i+1:]) + costs[j][i] for i in range(k)]

        return min(dp)


s = Solution()
print(s.minCostII([[1,5,3],[2,9,4]]))

