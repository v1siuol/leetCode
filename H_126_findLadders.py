"""
Success
Details 
Runtime: 488 ms, faster than 55.06% of Python3 online submissions for Word Ladder II.
Memory Usage: 16 MB, less than 54.29% of Python3 online submissions for Word Ladder II.
"""
from __future__ import annotations 
import collections 

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_dict = set(wordList)
        if endWord not in word_dict:
            return []

        res = []
        chars = 'abcdefghijklmnopqrstuvwxyz'

        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            next_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    res.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for c in chars:
                            next_word = word[:i]+c+word[i+1:]
                            if next_word in word_dict:
                                next_layer[next_word] += [j + [next_word] for j in layer[word]]
            word_dict -= set(next_layer.keys())
            layer = next_layer

        return res 


s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.findLadders(beginWord, endWord, wordList))


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(s.findLadders(beginWord, endWord, wordList))


beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
print(s.findLadders(beginWord, endWord, wordList))


# # bin dir bfs
# class Solution:
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         if endWord not in wordList or not endWord or not beginWord:
#             return []
#         wordList = set(wordList)
#         forward, backward = {beginWord}, {endWord}
#         direction = 1
#         parents = defaultdict(set)
#         while forward and backward:
#             if len(forward) > len(backward):
#                 forward, backward = backward, forward
#                 # We need to trace the direction in order to distinguish the parents
#                 direction *= -1
            
#             # The new set of words which will be forward in the next iteration
#             next_foward = set()
            
#             # Because all words in forward will be modified by one character
#             wordList -= forward
#             for word in forward:
#                 for i in range(len(word)):
#                     first, second = word[:i], word[i+1:]
#                     for ch in string.ascii_lowercase:
#                         combined_word = first + ch + second
#                         if combined_word in wordList:
#                             next_foward.add(combined_word)
#                             # Because at the last part, we find parents by indexing dictionary from endWord
#                             # So when direction == 1, the combined_word is the key
#                             # otherwise, the combined_word should be the value of dictionary.
#                             if direction == 1:
#                                 parents[combined_word].add(word)
#                             else:
#                                 parents[word].add(combined_word)
                                
#             # next_foward and backward are always in different direction,
#             # so if they have common elements we find a path.
#             # We check and return this function inside is because this problem finds the all shortest paths
#             if next_foward & backward:
#                 # Starting from the endWord, we find its parent and append to results
#                 # And do this until we reach the beginWord
#                 results = [[endWord]]
#                 while results[0][0] != beginWord:
#                     results = [ [parent] + result for result in results for parent in parents[result[0]] ]
#                 return results
#             forward = next_foward
#         return []
    
        