"""
Success
Details 
Runtime: 100 ms, faster than 24.29% of Python online submissions for Contains Duplicate II.
Memory Usage: 16.1 MB, less than 9.17% of Python online submissions for Contains Duplicate II.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 还可以dictionary留最近 
        windows = set()
        for i in range(len(nums)):
            if nums[i] in windows:
                return True
            else:
                windows.add(nums[i])
            if len(windows) > k:
                windows.remove(nums[i-k])

        return False


s = Solution()

nums = [1,2,3,1]
k = 3
print(s.containsNearbyDuplicate(nums, k))


nums = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))

