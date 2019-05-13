"""
Success
Details 
Runtime: 40 ms, faster than 92.56% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 14.5 MB, less than 9.09% of Python3 online submissions for Find the Duplicate Number.
"""
# Floyd's Tortoise and Hare (Cycle Detection)
class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast


s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
