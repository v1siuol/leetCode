from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 36 ms, faster than 81.19% of Python3 online submissions for Text Justification.
Memory Usage: 13.8 MB, less than 6.03% of Python3 online submissions for Text Justification.
"""

# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         res = []
#         count = 0
#         curr = []
#         for word in words:
#             if count + len(curr) + len(word) > maxWidth:
#                 # overflow 
#                 for i in range(maxWidth-count):
#                     curr[i % (len(curr)-1 or 1)] += ' '
#                 res.append(''.join(curr))
#                 count = 0
#                 curr = []
#             curr += [word]
#             count += len(word)
#         return res + [' '.join(curr).ljust(maxWidth)]


"""
Success
Details 
Runtime: 28 ms, faster than 99.07% of Python3 online submissions for Text Justification.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Text Justification.
"""
# respect.. 
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res = []
        curr_width = 0

        temp = []
        for word in words:

            n = len(word)
            if n + curr_width > maxWidth:
                gap = len(temp)-1
                if gap == 0:
                    temp_s = temp[0] + ' ' * ( maxWidth - len(temp[0]) )
                else:
                    left_space = maxWidth - curr_width + len(temp)
                    int_space = left_space // gap
                    spaces = [int_space] * gap
                    left_space = left_space % gap
                    space_i = 0
                    while left_space > 0:
                        spaces[space_i%gap] += 1
                        space_i += 1
                        left_space -= 1
                    temp_s = ''
                    for i in range(gap):
                        temp_s += temp[i] + ' '*spaces[i]
                    temp_s += temp[-1]
                res.append(temp_s)

                temp = []
                curr_width = 0

            temp.append(word)
            curr_width += n + 1

        last_row = ' '.join(temp)
        last_row += (maxWidth - len(last_row)) * ' '
        res.append(last_row)
        return res 
