"""
Success
Details 
Runtime: 132 ms, faster than 91.53% of Python3 online submissions for Range Addition.
Memory Usage: 21.8 MB, less than 44.12% of Python3 online submissions for Range Addition.
"""
from __future__ import annotations 

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # partial sum nb 
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc
            if end < length - 1:
                res[end+1] -= inc

        s = 0
        for i, p in enumerate(res):
            s += p
            res[i] = s

        return res


s = Solution()
# print(s.getModifiedArray(5, [[1 , 3 , 2] , [2, 3, 3]]))  # [0, 2, 5, 5, 0]
print(s.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))  # [-2,0,3,5,3] 

