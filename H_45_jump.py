"""
Success
Details 
Runtime: 64 ms, faster than 36.85% of Python3 online submissions for Jump Game II.
Memory Usage: 14.5 MB, less than 7.50% of Python3 online submissions for Jump Game II.
"""
class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        if len(nums) == 1:
            return 0 
        level = 0
        current_max = 0
        loc = 0
        next_max = 0
        goal = len(nums) - 1 

        while current_max >= loc:
            level += 1
            while loc <= current_max:
                next_max = max(next_max, loc + nums[loc])
                if next_max >= goal:
                    return level
                loc += 1
            current_max = next_max

        return -1 


s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([0]))
print(s.jump([2,1]))
print(s.jump([2,0,2,0,1]))
