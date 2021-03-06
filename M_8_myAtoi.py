from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 44 ms, faster than 95.28% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.5 MB, less than 5.34% of Python3 online submissions for String to Integer (atoi).
"""
# class Solution:
#     def myAtoi(self, str: 'str') -> 'int':
#         i = 0
#         n = len(str)
#         while i < n:
#             if str[i] == ' ':
#                 i += 1
#             else:
#                 break
#         if i == n:
#             return 0

#         is_neg = False

#         if str[i] == '-' or str[i] == '+':
#             if str[i] == '-':
#                 is_neg = True
#             i += 1

#         ret = 0
#         while i < n:
#             if str[i].isdigit():
#                 ret = ret * 10 + int(str[i])
#             else:
#                 break

#             i += 1

#         if is_neg:
#             ret = -2 ** 31 if ret > 2 ** 31 - 1 else -ret
#         else:
#             ret = 2 ** 31 - 1 if ret > 2 ** 31 - 1 else ret

#         return ret 


# s = Solution()
# print(s.myAtoi('42') == 42)
# print(s.myAtoi('   -42') == -42)
# print(s.myAtoi('4193 with words') == 4193)
# print(s.myAtoi('words and 987') == 0)
# print(s.myAtoi('-91283472332') == -2147483648)
# print(s.myAtoi('-2147483648') == -2147483648)
# print(s.myAtoi('2147483647') == 2147483647)
# print(s.myAtoi('    ') == 0)
# print(s.myAtoi('+1') == 1)
# print(s.myAtoi('-') == 0)
# print(s.myAtoi('-+1') == 0)



"""
Details 
Runtime: 36 ms, faster than 93.96% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.5 MB, less than 5.30% of Python3 online submissions for String to Integer (atoi).
"""

class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        sign = 1
        n = 0
        i = 0

        overflow = 2 ** 31 - 1 
        of = overflow // 10 

        while i < len(str) and str[i] == ' ':
            i += 1

        if i < len(str) and str[i] in '+-':
            if str[i] == '-':
                sign = -1 
            i += 1

        while i < len(str) and '0' <= str[i] <= '9':
            p = int(str[i])
            if n > of or (n == of and p > 7):
                return overflow if sign == 1 else - 2 ** 31 
            n = n * 10 + p
            i += 1

        return sign * n

