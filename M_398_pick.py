"""
Success
Details 
Runtime: 112 ms, faster than 40.18% of Python3 online submissions for Random Pick Index.
Memory Usage: 18.3 MB, less than 6.52% of Python3 online submissions for Random Pick Index.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 


class Solution:

    def __init__(self, nums: List[int]):
        self.dct = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            self.dct[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.dct[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()