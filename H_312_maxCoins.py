"""
Success
Details 
Runtime: 472 ms, faster than 53.29% of Python3 online submissions for Burst Balloons.
Memory Usage: 13.5 MB, less than 75.06% of Python3 online submissions for Burst Balloons.
"""
class Solution:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        # 神仙打架 
        lst = [1] + [i for i in nums if i > 0] + [1]
        n = len(lst)
        dp = [[0] * n for _ in range(n)]

        for length in range(n):
            for start in range(1, n-length-1):
                end = start + length
                for pivot in range(start, end+1):
                    dp[start][end] = max(dp[start][end], 
                        dp[start][pivot-1] + dp[pivot+1][end] + lst[start-1] * lst[pivot] * lst[end+1])

        return dp[1][n-2]


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
