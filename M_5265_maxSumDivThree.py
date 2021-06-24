from __future__ import annotations 
import collections 
import random 
import heapq 


# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         d = collections.defaultdict(list)

#         for num in nums:
#             if num <= 0:
#                 continue
#             d[num%3].append(num)

#         m1 = sorted(d[1], reverse=True)
#         m2 = sorted(d[2], reverse=True)

#         s = sum(d[0])

#         # for i in range(min(len(m1), len(m2))):
#         #     s += m1[i] + m2[i]

#         i1 = 0
#         i2 = 0
#         while i1 < len(m1) and i2 < len(m2):

#             t1 = -1
#             if i1 <= len(m1) - 3:
#                 # 3 
#                 t1 = m1[i1] + m1[i1+1] + m1[i1+2] 

#             t2 = -1
#             if i2 <= len(m2) - 3:
#                 # 3 
#                 t2 = m2[i2] + m2[i2+1] + m2[i2+2] 

#             t3 = m1[i1] +m2[i2]

#             t_max = max(t1, t2, t3)
#             if t3 == t_max:
#                 i1 += 1
#                 i2 += 1
#             elif t2 == t_max:
#                 i2 += 3
#             else:
#                 i1 += 3

#             s += t_max

#         while i1 <= len(m1) - 3:
#             s += m1[i1] + m1[i1+1] + m1[i1+2] 
#             i1 += 3

#         while i2 <= len(m2) - 3:
#             s += m2[i2] + m2[i2+1] + m2[i2+2] 
#             i2 += 3

#         return s






class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)

        for num in nums:
            if num <= 0:
                continue
            d[num%3].append(num)

        m1 = sorted(d[1], reverse=True)
        m2 = sorted(d[2], reverse=True)

        s = sum(d[0])
        total = sum(m1) + sum(m2)
        curr_mod = total % 3

        if curr_mod == 0:
            return total + s

        if curr_mod == 1:
            mi = float('inf')
            if len(m2) >= 2:
                mi = m2[-1] + m2[-2]
            if len(m1) >= 1:
                mi = min(mi, m1[-1])

            if mi == float('inf'):
                return s
            else:
                return s+total-mi 

        if curr_mod == 2:
            mi = float('inf')
            if len(m1) >= 2:
                mi = m1[-1] + m1[-2]
            if len(m2) >= 1:
                mi = min(mi, m2[-1])

            if mi == float('inf'):
                return s
            else:
                return s+total-mi 


s = Solution()

# [3,6,5,1,8]
print(s.maxSumDivThree([3,6,5,1,8]) == 18)

# # [2,6,2,2,7]
# print(s.maxSumDivThree([2,6,2,2,7]))
print(s.maxSumDivThree([2,6,2,2,7]) == 15)

# [5,2,2,2]
print(s.maxSumDivThree([5,2,2,2]) == 9)

# [366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]
print(s.maxSumDivThree([366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]) == 50487)
# print(s.maxSumDivThree([366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]))