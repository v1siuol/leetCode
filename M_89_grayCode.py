from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 104 ms, faster than 82.37% of Python3 online submissions for Gray Code.
Memory Usage: 21.7 MB, less than 54.84% of Python3 online submissions for Gray Code.
Areas of improvement: 复杂 位运算 规律
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def generate_list_by_gap():
            ret = [0]
            for gap in gap_list:
                ret.append(ret[-1] + gap)
            return ret
        gap_list = [1]
        for i in range(1, n):
            lead = 2 ** i
            back = [-x for x in reversed(gap_list)]
            gap_list.append(lead)
            gap_list.extend(back)
        return generate_list_by_gap()

print(Solution().grayCode(2))
print(Solution().grayCode(3))
