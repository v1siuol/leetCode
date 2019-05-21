"""
Success
Details 
Runtime: 36 ms, faster than 99.38% of Python3 online submissions for Triangle.
Memory Usage: 13.5 MB, less than 75.01% of Python3 online submissions for Triangle.
"""
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # bottom up 
        dp = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for node in range(i+1):
                dp[node] = min(dp[node], dp[node+1]) + triangle[i][node]

        return dp[0]



s = Solution()
tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(tri))
# print(s.minimumTotal(tri) == 11)

