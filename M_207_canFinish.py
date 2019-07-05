"""
Success
Details 
Runtime: 48 ms, faster than 76.74% of Python3 online submissions for Course Schedule.
Memory Usage: 16.4 MB, less than 24.89% of Python3 online submissions for Course Schedule.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        todo = [0] * numCourses
        done = [0] * numCourses

        def acyclic(i):
            if todo[i]:
                return False
            if done[i]:
                return True
            todo[i] = done[i] = 1
            for v in graph[i]:
                if not acyclic(v):
                    return False
            todo[i] = 0
            return True 

        for i in range(numCourses):
            if not done[i] and not acyclic(i):
                return False
        return True 


s = Solution()
ans = s.canFinish(2, [[1,0]])
exp = True
print(ans, ans == exp)

ans = s.canFinish( 2, [[1,0],[0,1]])
exp = False
print(ans, ans == exp)
