"""
Success
Details 
Runtime: 20 ms, faster than 81.03% of Python online submissions for Pascal's Triangle II.
Memory Usage: 11.8 MB, less than 5.95% of Python online submissions for Pascal's Triangle II.
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0 for _ in range(rowIndex+1)]
        res[0] = 1
        for i in range(rowIndex+1):
            j = i
            while j >= 1:
                res[j] += res[j-1]
                j -= 1

        return res


s = Solution()
print(s.getRow(3))
print(s.getRow(5))
