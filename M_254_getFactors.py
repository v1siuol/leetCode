"""
Success
Details 
Runtime: 2324 ms, faster than 18.59% of Python3 online submissions for Factor Combinations.
Memory Usage: 13.1 MB, less than 74.20% of Python3 online submissions for Factor Combinations.
"""
class Solution:
    def getFactors(self, n: 'int') -> 'List[List[int]]':
        # 有更快的解法 
        ret = []
        backtrack(2, n, [], ret)
        return ret


def backtrack(start, n, path, result):
    if n == 1:
        if len(path) > 1:
            result.append(path)
        return

    for i in range(start, n+1):
        if n % i == 0:
            backtrack(i, n//i, path+[i], result)


s = Solution()
print(s.getFactors(1))
print(s.getFactors(37))
print(s.getFactors(12))
print(s.getFactors(32))

