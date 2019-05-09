"""
Success
Details 
Runtime: 32 ms, faster than 12.08% of Python online submissions for Pascal's Triangle.
Memory Usage: 11.8 MB, less than 5.26% of Python online submissions for Pascal's Triangle.
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            temp = [None for _ in range(i+1)]
            temp[0], temp[-1] = 1, 1

            for j in range(1, i):
                temp[j] = res[-1][j-1] + res[-1][j]

            res.append(temp)
        return res



s = Solution()
print(s.generate(5))

