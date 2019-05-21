"""
Success
Details 
Runtime: 36 ms, faster than 99.40% of Python3 online submissions for Next Permutation.
Memory Usage: 13.3 MB, less than 20.98% of Python3 online submissions for Next Permutation.
"""

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums 不为空
        j = len(nums) - 1
        while j > 0:
            if nums[j] > nums[j-1]:
                # find
                break
            j -= 1

        if j > 0:
            l_min_pos = j - 1 
            swap_next_pos = j + 1 
            # curr is smaller than l_min
            while swap_next_pos < len(nums):
                if nums[swap_next_pos] <= nums[l_min_pos]:
                    break
                swap_next_pos += 1
            swap_next_pos -= 1
            nums[l_min_pos], nums[swap_next_pos] = nums[swap_next_pos], nums[l_min_pos]
            # print(l_min_pos, j, swap_next_pos, nums)

        # all reverse 
        if j == 0:
            l_min_pos = -1


        left = l_min_pos + 1
        right = len(nums) - 1

        # reverse
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



s = Solution()
lst = [1, 2, 3]
s.nextPermutation(lst)
print(lst)


lst = [3, 2, 1]
s.nextPermutation(lst)
print(lst)

lst = [1, 1, 5]
s.nextPermutation(lst)
print(lst)

lst = [1]
s.nextPermutation(lst)
print(lst)


lst = [1, 5, 1]
s.nextPermutation(lst)
print(lst)

