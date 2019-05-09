"""
Success
Details 
Runtime: 48 ms, faster than 95.78% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.2 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array II.
"""


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':

        def remove_k_dup(nums, k):
            n = len(nums)
            if n <= k:
                return n

            i = 0
            res = 0
            dup_counter = 1
            while i < n-1:
                if nums[i] == nums[i+1]:
                    if dup_counter < k:
                        res += 1
                        i += 1
                    else:
                        nums.pop(i+1)
                        n -= 1
                    dup_counter += 1
                else:
                    dup_counter = 1
                    res += 1
                    i += 1

            return res + 1

        return remove_k_dup(nums, 2)


s = Solution()

nums = [1,1,1,2,2,3]
print(s.removeDuplicates(nums), nums)


nums = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(nums), nums)

