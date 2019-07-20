"""
Success
Details 
Runtime: 208 ms, faster than 45.65% of Python3 online submissions for Range Sum Query - Mutable.
Memory Usage: 22.4 MB, less than 12.01% of Python3 online submissions for Range Sum Query - Mutable.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None 
        self.sum = 0


class NumArray:
    # segment tree god 

    def __init__(self, nums: List[int]):
        self.root = self._build_tree(nums, 0, len(nums)-1)

    def update(self, i: int, val: int) -> None:
        self._update(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self._sum_range(self.root, i, j)

    def _build_tree(self, nums, start, end):
        if start > end:
            return None
        ret = Node(start, end)
        if start == end:
            ret.sum = nums[start]
        else:
            mid = (start + end) // 2
            ret.left = self._build_tree(nums, start, mid)
            ret.right = self._build_tree(nums, mid+1, end)
            ret.sum = ret.left.sum + ret.right.sum
        return ret 

    def _update(self, root, pos, val):
        if root.start == root.end:
            root.sum = val
        else:
            mid = (root.start + root.end) // 2 
            if pos <= mid:
                self._update(root.left, pos, val)
            else:
                self._update(root.right, pos, val)
            root.sum = root.left.sum + root.right.sum

    def _sum_range(self, root, start, end):
        if root.end == end and root.start == start:
            return root.sum
        else:
            mid = (root.start + root.end) // 2
            if end <= mid:
                return self._sum_range(root.left, start, end)
            elif start >= mid+1:
                return self._sum_range(root.right, start, end)
            else:
                return self._sum_range(root.right, mid+1, end) + self._sum_range(root.left, start, mid)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)