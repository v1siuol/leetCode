from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect




class Solution:
    def longestDecomposition(self, text: str) -> int:
        # greety
        i = 0
        j = len(text) - 1
        front_set = collections.defaultdict(int)
        tail_set = collections.defaultdict(int)
        count = 0

        while i <= j:

            # front_set.add(text[i])
            # tail_set.add(text[j])

            front_set[text[i]] += 1
            tail_set[text[j]] += 1

            # print(front_set, tail_set, count)
            if front_set == tail_set:
                if i == j:
                    count += 1
                else:
                    count += 2
                front_set.clear()
                tail_set.clear()

            i += 1
            j -= 1

        if len(front_set) > 0:
            count += 1

        return count 




s = Solution()

text = "ghiabcdefhelloadamhelloabcdefghi"
print(s.longestDecomposition(text))

text = "merchant"
print(s.longestDecomposition(text))

text = "antaprezatepzapreanta"
print(s.longestDecomposition(text))

text = "aaa"
print(s.longestDecomposition(text))

text = "ctbqeflelkkefleltbqc"
print(s.longestDecomposition(text))
