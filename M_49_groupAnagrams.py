from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 136 ms, faster than 29.64% of Python3 online submissions for Group Anagrams.
Memory Usage: 18 MB, less than 5.82% of Python3 online submissions for Group Anagrams.
"""

# class Solution:
#     def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
#         anagram = collections.defaultdict(list)
#         for word in strs:
#             ids = [0 for _ in range(26)]
#             for s in word:
#                 ids[ord(s) - 97] += 1

#             anagram[tuple(ids)].append(word)

#         return list(anagram.values())


# s = Solution()
# print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(s.groupAnagrams(["and","dan"]))


"""
Success
Details 
Runtime: 112 ms, faster than 85.44% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.5 MB, less than 20.87% of Python3 online submissions for Group Anagrams.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass
        dct = collections.defaultdict(list)
        for word in strs:
            dct[tuple(sorted(word))].append(word)
        return list(dct.values())

