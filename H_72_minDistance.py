"""
Success
Details 
Runtime: 240 ms, faster than 18.48% of Python3 online submissions for Edit Distance.
Memory Usage: 16.8 MB, less than 54.87% of Python3 online submissions for Edit Distance.
"""
class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        # 有用一维 有用heap.. 
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]

        for i in range(1, l1+1):
            dp[i][0] = i

        for j in range(1, l2+1):
            dp[0][j] = j

        # print(dp)

        for m in range(1, l1+1):
            for n in range(1, l2+1):
                dp[m][n] = min(dp[m-1][n], dp[m][n-1]) + 1

                if word1[m-1] == word2[n-1]:
                    dp[m][n] = min(dp[m][n], dp[m-1][n-1])
                else:
                    dp[m][n] = min(dp[m][n], dp[m-1][n-1]+1)

        return dp[l1][l2]



s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("", "ros"))
print(s.minDistance("12", ""))
print(s.minDistance("intention", "execution"))
