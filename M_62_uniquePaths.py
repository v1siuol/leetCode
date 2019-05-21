"""
Success
Details 
Runtime: 40 ms, faster than 41.05% of Python3 online submissions for Unique Paths.
Memory Usage: 13.3 MB, less than 12.45% of Python3 online submissions for Unique Paths.
"""
class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        if m == 1 or n == 1:
            return 1
        m -= 1
        n -= 1

        # swap to larger m
        if m < n:
            m = m + n
            n = m - n
            m = m - n

        # cal comb
        res = 1
        j = 1

        for i in range(m+1, m+n+1):
            res *= i
            res /= j
            j += 1

        return int(res)



s = Solution()
print(s.uniquePaths(3, 2))
print(s.uniquePaths(7, 3))
print(s.uniquePaths(1, 3))
