from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 28 ms, faster than 97.91% of Python3 online submissions for Decode String.
Memory Usage: 13.3 MB, less than 25.00% of Python3 online submissions for Decode String.
"""
# class Solution:
#     def decodeString(self, s: str) -> str:
#         res = ''
#         count_stack = collections.deque()
#         res_stack = collections.deque()
#         idx = 0

#         while idx < len(s):
#             if s[idx] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
#                 num = 0
#                 while s[idx] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
#                     num = 10 * num +  int(s[idx])
#                     idx += 1
#                 count_stack.append(num)
#             elif s[idx] == '[':
#                 res_stack.append(res)
#                 res = ''
#                 idx += 1
#             elif s[idx] == ']':
#                 num = count_stack.pop()
#                 temp = res_stack.pop()
#                 res = temp + res * num
#                 idx += 1  
#             else:
#                 res += s[idx]
#                 idx += 1 
#         return res 






# s = Solution()


# s1 = "3[a]2[bc]"
# print(s.decodeString(s1))

# s1 = "3[a2[c]]"
# print(s.decodeString(s1))

# s1 = "2[abc]3[cd]ef"
# print(s.decodeString(s1))


"""
  1.使用两个栈，countStack存子串的重复次数，resStack存中间结果
  2.读取完一个数字，把数量入countStack栈
  3.读取到[时，把n[前面的结果计算出来并入resStack栈
  4.读取到]时，取出最近一次n[res]前面的中间计算结果，也就是resStack的栈顶，再append n次res，n为countStack的栈顶，res为最近一次[]中间的子串
  5.其他情况，将字符追加到res末尾
 
  比如:  3[a]2[b3[d]c]
 下面是读完各字符时的情况：
 *        读完:  3    [     a     ]     2    [    b      3       [      d       ]      c       ]
 * countStack: (3)  (3)   (3)    ()   (2)  (2)  (2)   (2 3)   (2 3)   (2 3)   (2)    (2)      ()
 *   resStack: ()   ("")  ("")   ()   ()  (aaa) (aaa) (aaa)  (aaa b) (aaa b)  (aaa) (aaa)     ()
 *        res: ""    ""    a     aaa  aaa   ""   b      b       ""     d      bddd  bdddc  aaabdddcbdddc
"""


"""
Success
Details 
Runtime: 28 ms, faster than 96.86% of Python3 online submissions for Decode String.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decode String.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = collections.deque()
        res_stack = collections.deque()
        res = ''
        temp_int = 0
        for char in s:
            if '0' <= char <= '9':
                if temp_int != 0:
                    temp_int = temp_int * 10 + int(char)
                else:
                    temp_int = int(char)
            elif char == '[':
                count_stack.append(temp_int)
                temp_int = 0
                res_stack.append(res)
                res = ''
            elif char == ']':
                n = count_stack.pop()
                prev = res_stack.pop()
                res = prev + n * res
            else:
                res += char
        return res
