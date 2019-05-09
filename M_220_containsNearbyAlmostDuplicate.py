"""
Success
Details 
Runtime: 56 ms, faster than 37.56% of Python3 online submissions for Contains Duplicate III.
Memory Usage: 15.4 MB, less than 7.69% of Python3 online submissions for Contains Duplicate III.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: 'int', t: 'int') -> 'bool':
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        tt = t + 1
        windows = dict()

        for i, val in enumerate(nums):
            slot = val // tt
            if slot in windows:
                return True
            elif slot-1 in windows and abs(val-windows[slot-1]) <= t:
                return True
            elif slot+1 in windows and abs(val-windows[slot+1]) <= t:
                return True
            else:
                windows[slot] = val

            if len(windows) > k:
                del windows[nums[i-k]//tt]

        return False


s = Solution()


nums = [1,2,3,1]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k ,t) == True)

nums = [1,0,1,1]
k = 1
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k ,t) == True)


nums = [1,5,9,1,5,9]
k = 2
t = 3
print(s.containsNearbyAlmostDuplicate(nums, k ,t) == False)


nums = [-1,-1]
k = 1
t = -1
print(s.containsNearbyAlmostDuplicate(nums, k ,t) == False)



nums = [2,1]
k = 1
t = 1
print(s.containsNearbyAlmostDuplicate(nums, k ,t) == True)


nums = [2,0,-2,2]
k = 2
t = 1
print(s.containsNearbyAlmostDuplicate(nums, k ,t) == False)

