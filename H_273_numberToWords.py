from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 32 ms, faster than 99.49% of Python3 online submissions for Integer to English Words.
Memory Usage: 13.4 MB, less than 19.67% of Python3 online submissions for Integer to English Words.
"""
# class Solution:
#     # 写太复杂了 

#     to_19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
#             'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
#             'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
#     to_90 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
#     to_000 = ['Ten', 'Hundred', 'Thousand', 'Million', 'Billion']

#     def numberToWords(self, num: 'int') -> 'str':
        
#         num_str = str(num)
#         ret = ''
#         billion = num_str[-10:-9]
#         if billion != '':
#             ret += self.helper(int(billion)) + ' ' + self.to_000[4] + ' '
#         million = num_str[-9:-6]
#         if million != '':
#             _million = self.helper(int(million)) 
#             if _million != '':
#                 ret += _million + ' ' + self.to_000[3] + ' '
#         thousand = num_str[-6:-3]
#         if thousand != '':
#             _thousand = self.helper(int(thousand))
#             if _thousand != '':
#                 ret += _thousand + ' ' + self.to_000[2] + ' ' 

#         one = num_str[-3:]
#         if one != '':
#             one_str =  self.helper(int(one))
#             ret += one_str
#             if one_str == '':
#                 ret = ret[:-1]

#         return ret if ret else 'Zero'

#     def helper(self, num):

#         ret = ''
#         hundred = num // 100
#         if hundred > 0:
#             ret += self.to_19[hundred-1] + ' ' + self.to_000[1] + ' ' 

#         last_two = num % 100
#         if last_two >= 20:
#             ten = last_two // 10
#             ret += self.to_90[ten-1]
#             one = last_two % 10
#             if one > 0:
#                 ret += ' ' + self.to_19[one-1]

#         elif last_two > 0:
#             ret += self.to_19[last_two-1]
#         else:
#             ret = ret[:-1]
#         return ret


# s = Solution()
# print(s.numberToWords(123) == "One Hundred Twenty Three")
# print(s.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five")
# print(s.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
# print(s.numberToWords(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
# print(s.numberToWords(100))
# print(s.numberToWords(0))
# print(s.numberToWords(1000))
# print(s.numberToWords(10100))
# print(s.numberToWords(1000000))


"""
Success
Details 
Runtime: 24 ms, faster than 99.93% of Python3 online submissions for Integer to English Words.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer to English Words.
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        s = ['DUMP', 'Thousand', 'Million', 'Billion']
        res = collections.deque()
        level = 0
        if num == 0:
            return 'Zero'
        while num != 0:
            last3 = num % 1000
            num //= 1000
            if last3 != 0:
                if level > 0:
                    res.appendleft(s[level])
                res.appendleft(d100(last3))

            level += 1

        return ' '.join(res)

def d100(n):
    d1 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    # 100
    temp = []
    h = n // 100

    if h != 0:
        temp.append(d1[h])
        temp.append('Hundred')

    t = (n // 10) % 10
    if t != 0:
        if t == 1:
            # 10-19
            d = n % 10
            d11 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
            temp.append(d11[d])
        else:
            # 20 - 99
            d12 = ['DUMP', 'DUMP', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            temp.append(d12[t])

    if t != 1:
        d = n % 10
        if d != 0:
            temp.append(d1[d])

    return ' '.join(temp)
