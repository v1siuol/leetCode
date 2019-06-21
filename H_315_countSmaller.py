"""
Success
Details 
Runtime: 152 ms, faster than 60.17% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 18 MB, less than 19.64% of Python3 online submissions for Count of Smaller Numbers After Self.
"""
from __future__ import annotations 

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # bisect 

        def sort(enum):
            half = len(enum) // 2
            if half > 0:
                left, right = sort(enum[:half]), sort(enum[half:])

                for i in range(len(enum)-1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        res[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum     

        res = [0] * len(nums)
        sort(list(enumerate(nums)))
        return res



s = Solution()
print(s.countSmaller([5,2,6,1]))  # [2,1,1,0]
