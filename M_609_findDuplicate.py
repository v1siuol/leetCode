from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 92 ms, faster than 100.00% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 23.4 MB, less than 15.04% of Python3 online submissions for Find Duplicate File in System.
"""

# class Solution:
#     def findDuplicate(self, paths: List[str]) -> List[List[str]]:
#         content2path = collections.defaultdict(list)
#         for path in paths:
#             lst = path.split()
#             for content in lst[1:]:
#                 tmp = content.split('(')
#                 # 1 -1 去掉 ) 
#                 content2path[tmp[1][:-1]].append(lst[0]+'/'+tmp[0])
#         return [vals for vals in content2path.values() if len(vals) > 1]


"""
Success
Details 
Runtime: 88 ms, faster than 98.43% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 22.6 MB, less than 72.73% of Python3 online submissions for Find Duplicate File in System.
"""
# 找重dictionary 
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = collections.defaultdict(list)
        for path in paths:
            p = path.split()
            dirt = p[0]
            for content in p[1:]:
                file_name, content = content.split('(')
                store[content[:-1]].append(dirt+'/'+file_name)

        return [vals for vals in store.values() if len(vals) > 1]
