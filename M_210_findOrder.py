"""
Success
Details 
Runtime: 52 ms, faster than 77.16% of Python3 online submissions for Course Schedule II.
Memory Usage: 14.4 MB, less than 66.74% of Python3 online submissions for Course Schedule II.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        can_take = collections.defaultdict(set)
        in_deg = [0] * numCourses
        for after, pre in prerequisites:
            can_take[pre].add(after)
            in_deg[after] += 1

        stack = [i for i,cnt in enumerate(in_deg) if cnt == 0]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in can_take[node]:
                in_deg[i] -= 1
                if in_deg[i] == 0:
                    stack.append(i)

        return [] if sum(in_deg) > 0 else res 


s = Solution()
ans = s.findOrder(2, [[1,0]])
exp = [0,1]
print(ans, ans == exp)

ans = s.findOrder( 4, [[1,0],[2,0],[3,1],[3,2]])
exp = [0,2,1,3]
print(ans, ans == exp)

ans = s.findOrder( 2, [])
exp = [1,0]
print(ans, ans == exp)
