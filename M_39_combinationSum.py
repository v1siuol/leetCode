from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 100 ms, faster than 49.07% of Python3 online submissions for Combination Sum.
Memory Usage: 13.4 MB, less than 15.12% of Python3 online submissions for Combination Sum.
"""

# class Solution:
#     def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
#         # 盲打一个套路？ 
#         def backtrack(target, start=0, lst=[]):
#             if target == 0:
#                 ret.append(lst[:])
#             elif target < 0:
#                 return
#             else:
#                 for i in range(start, n):
#                     lst.append(candidates[i])
#                     backtrack(target-candidates[i], i, lst)
#                     lst.pop()


#         ret = []
#         n = len(candidates)
#         # candidates.sort()
#         backtrack(target, 0)
#         return ret

        
# s = Solution()
# print(s.combinationSum([2,3,6,7],7))
# print(s.combinationSum([7,2,3,6],7))
# print(s.combinationSum([2,3,5],8))


"""
Success
Details 
Runtime: 60 ms, faster than 90.98% of Python3 online submissions for Combination Sum.
Memory Usage: 13.8 MB, less than 5.05% of Python3 online submissions for Combination Sum.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        backtracking(candidates, target, 0, [], ret)
        return ret 


def backtracking(candidates, target, idx, path, ret):
    if target == 0:
        ret.append(path)
        return 
    for i, num in enumerate(candidates[idx:]):
        left = target - num
        if left >= 0:
            backtracking(candidates, left, i+idx, path+[num], ret)
        else:
            break
