"""
Success
Details 
Runtime: 104 ms, faster than 74.14% of Python3 online submissions for Unique Word Abbreviation.
Memory Usage: 17.9 MB, less than 94.12% of Python3 online submissions for Unique Word Abbreviation.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = dict()
        for word in dictionary:
            w = self.encode(word)
            if w in self.words and self.words[w] != '' and self.words[w] != word:
                self.words[w] = ''
            else:
                self.words[w] = word

    def isUnique(self, word: str) -> bool:
        w = self.encode(word)
        return w not in self.words or self.words[w] == word

    def encode(self, word):
        n = len(word)
        if n < 3:
            return word
        return word[0]+str(n-2)+word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)