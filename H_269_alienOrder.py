from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 36 ms, faster than 87.00% of Python3 online submissions for Alien Dictionary.
Memory Usage: 13.1 MB, less than 72.82% of Python3 online submissions for Alien Dictionary.
"""

# class Solution:
#     def alienOrder(self, words: List[str]) -> str:
#         graph = collections.defaultdict(set)
#         # in_degree_map = collections.defaultdict(int)
#         in_degree_map = dict()
#         for word in words:
#             for c in word:
#                 in_degree_map[c] = 0

#         for i in range(len(words)-1):
#             curr_word = words[i]
#             next_word = words[i+1]
#             min_len = min(len(curr_word), len(next_word))
#             for j in range(min_len):
#                 curr_char = curr_word[j]
#                 next_char = next_word[j]
#                 if curr_char != next_char:
#                     # if curr_char not in graph:
#                     #     graph[curr_char] = dict()
#                     # curr_set = graph[curr_char]
#                     if next_char not in graph[curr_char]:
#                         # curr_set.add(next_char)
#                         graph[curr_char] |= set(next_char)
#                         in_degree_map[next_char] += 1
#                     break

#         stack = []
#         for key, val in in_degree_map.items():
#             if val == 0:
#                 stack.append(key)

#         # BFS
#         res = []
#         while stack:
#             curr_char = stack.pop()
#             res.append(curr_char)
#             if curr_char in graph:
#                 for next_char in graph[curr_char]:
#                     in_degree_map[next_char] -= 1
#                     if in_degree_map[next_char] == 0:
#                         stack.append(next_char)

#         return '' if sum(in_degree_map.values()) > 0 else ''.join(res)


# s = Solution()

# ans = s.alienOrder(["wrt","wrf","er","ett","rftt"])
# exp = "wertf"
# print(ans, ans == exp)



"""
Success
Details 
Runtime: 32 ms, faster than 97.69% of Python3 online submissions for Alien Dictionary.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Alien Dictionary.
"""
# in degree + stack BFS 
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        after_key = collections.defaultdict(set)
        in_degree = dict()

        for word in words:
            for char in word:
                in_degree[char] = 0

        for i in range(len(words)-1):
            curr_word = words[i]
            next_word = words[i+1]
            for j in range(min(len(curr_word), len(next_word))):
                curr_char = curr_word[j]
                next_char = next_word[j]
                if curr_char != next_word[j]:
                    if next_char not in after_key[curr_char]:
                        after_key[curr_char].add(next_char)
                        in_degree[next_char] += 1
                    break

        stack = collections.deque()
        for key, val in in_degree.items():
            if val == 0:
                stack.append(key)

        res = ''
        while stack:
            curr = stack.pop()
            res += curr

            for char in after_key[curr]:
                in_degree[char] -= 1
                if in_degree[char] == 0:
                    stack.append(char)

        return '' if sum(in_degree.values()) > 0 else res 
