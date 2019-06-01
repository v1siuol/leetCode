"""
Success
Details 
Runtime: 44 ms, faster than 70.61% of Python3 online submissions for Interleaving String.
Memory Usage: 13.2 MB, less than 55.35% of Python3 online submissions for Interleaving String.
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 难 
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [False] * (len(s2) + 1)
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1] or dp[j] and s1[i-1] == s3[i+j-1]

        return dp[len(s2)]



s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1, s2, s3))

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(s.isInterleave(s1, s2, s3))
