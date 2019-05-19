"""
Success
Details 
Runtime: 96 ms, faster than 48.39% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.3 MB, less than 29.91% of Python3 online submissions for Combination Sum II.
"""
class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        def backtrack(target, start, path, ret):
            if target < 0:
                return
            elif target == 0:
                ret.append(path)
                return 
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue

                    backtrack(target-candidates[i], i+1, path+[candidates[i]], ret)


        ret = []
        candidates.sort()
        backtrack(target, 0, [], ret)
        return ret



s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# print(s.combinationSum2([2,5,2,1,2], 5))

