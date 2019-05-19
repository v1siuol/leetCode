"""
Success
Details 
Runtime: 32 ms, faster than 99.16% of Python3 online submissions for Combination Sum III.
Memory Usage: 13.2 MB, less than 44.31% of Python3 online submissions for Combination Sum III.
"""
class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        result = []
        backtrack(1, n, [], result, k)
        return result

def backtrack(start, target, path, result, k):
    if k == 0 and target == 0:
        result.append(path)
        return
    if k <= 0:
        return
    for i in range(start, 10):
        if i > target:
            break
        backtrack(i+1, target-i, path+[i], result, k-1)


s = Solution()
# print(s.combinationSum3(3, 7))
print(s.combinationSum3(3, 9))
