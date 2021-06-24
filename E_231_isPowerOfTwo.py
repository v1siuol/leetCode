from __future__ import annotations 
import collections 
import random 
import heapq 

"""
1108 / 1108 test cases passed.
Status: Accepted
Runtime: 52 ms
You are here!
Your runtime beats 49.18% of python submissions.
"""
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         #print(bin(n))
#         return bin(n).count("1") == 1 if n > 0 else False

# print(Solution().isPowerOfTwo(8))
# print(Solution().isPowerOfTwo(-16))


"""
Success
Details 
Runtime: 28 ms, faster than 94.09% of Python3 online submissions for Power of Two.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Two.
"""
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         # O(log n) O(1) 
#         while n > 1 and n % 2 == 0:
#             n //= 2
            
#         return n == 1

"""
Success
Details 
Runtime: 24 ms, faster than 98.24% of Python3 online submissions for Power of Two.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Power of Two.
"""
# bit opr 更快
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # O(1) O(1)
        if n <= 0:
            return False
        return n & (n-1) == 0
