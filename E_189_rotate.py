"""
Success
Details 
Runtime: 52 ms, faster than 56.28% of Python online submissions for Rotate Array.
Memory Usage: 12.3 MB, less than 5.01% of Python online submissions for Rotate Array.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 跳针再巧妙一点就过
        n = len(nums)
        k %= n
        reverse_list_inplace(nums, 0, n)
        reverse_list_inplace(nums, 0, k)
        reverse_list_inplace(nums, k, n)

def reverse_list_inplace(lst, start, end):
    for i in range((end-start)//2):
        lst[start+i], lst[end-(i+1)] = lst[end-(i+1)], lst[start+i]


s = Solution()

nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)


nums = [-1,-100,3,99]
print(s.rotate(nums, 2), nums)
nums = [-1,-100,3,99]
print(s.rotate(nums, 0), nums)
nums = [-1,-100,3,99]
print(s.rotate(nums, 6), nums)



nums = [1,2,3,4,5,6]
s.rotate(nums, 2)
print(nums)