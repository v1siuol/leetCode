"""
Success
Details 
Runtime: 80 ms, faster than 97.14% of Python3 online submissions for Word Ladder.
Memory Usage: 13.8 MB, less than 83.58% of Python3 online submissions for Word Ladder.
"""
from __future__ import annotations 
import collections 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        word_dict = set(wordList)
        if endWord not in word_dict:
            return 0 
        begin_set = set()
        end_set = set()
        chars = 'abcdefghijklmnopqrstuvwxyz'
        visited = set()
        res = 1 

        begin_set.add(beginWord)
        end_set.add(endWord)

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            temp = set()
            for word in begin_set:
                for i in range(len(word)):
                    for c in chars:
                        next_word = word[:i]+c+word[i+1:]
                        if next_word in end_set:
                            return res+1

                        if next_word not in visited and next_word in word_dict:
                            temp.add(next_word)
                            visited.add(next_word)
            begin_set = temp
            res += 1

        return 0 



s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.ladderLength(beginWord, endWord, wordList))  # 5

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(s.ladderLength(beginWord, endWord, wordList))  # 0 
