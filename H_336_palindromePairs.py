from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 944 ms, faster than 22.29% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 21 MB, less than 5.85% of Python3 online submissions for Palindrome Pairs.
"""

# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         # 不明所以 
#         res = []
#         root = Node()

#         for idx, word in enumerate(words):
#             add_word(root, word, idx)

#         for idx, word in enumerate(words):
#             search(root, word, idx, res)

#         return res 

# class Node:
#     def __init__(self):
#         self.children = collections.defaultdict(Node)
#         self.idx = -1  # is_word 
#         self.lst = []

# def is_palindrome(word, i, j):
#     while i < j:
#         if word[i] != word[j]:
#             return False
#         i += 1
#         j -= 1
#     return True 

# def add_word(root, word, idx):
#     for i in reversed(range(len(word))):
#         if is_palindrome(word, 0, i):
#             root.lst.append(idx)
#         root = root.children[word[i]]

#     root.lst.append(idx)
#     root.idx = idx

# def search(root, word, idx, res):
#     for j in range(len(word)):
#         if root.idx >= 0 and root.idx != idx and is_palindrome(word, j, len(word)-1):
#             res.append([idx, root.idx])
#         root = root.children.get(word[j])
#         if root is None:
#             return 

#     for j in root.lst:
#         if idx == j:
#             continue 
#         res.append([idx, j])


"""
Success
Details 
Runtime: 360 ms, faster than 99.74% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Palindrome Pairs.
"""
# reverse 左右秒啊 
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse = dict()
        for i, word in enumerate(words):
            reverse[word[::-1]] = i
        res = []
        for i, word in enumerate(words):
            n = len(word)

            for j in range(n):
                l, r = word[:j], word[j:]
                if l in reverse and r == r[::-1] and reverse[l] != i:
                    res.append([i, reverse[l]])
                    if l == '':
                        res.append([reverse[l], i])
                if r in reverse and l == l[::-1] and reverse[r] != i:
                    res.append([reverse[r], i])
                    if r == '':
                        res.append([i, reverse[r]])
        return res 
