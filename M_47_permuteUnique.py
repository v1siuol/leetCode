"""
Success
Details 
Runtime: 72 ms, faster than 82.53% of Python3 online submissions for Permutations II.
Memory Usage: 13.4 MB, less than 33.71% of Python3 online submissions for Permutations II.
"""
class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        ret = []
        n = len(nums)
        backtrack(nums, [], ret, [False]*n, n)
        return ret


def backtrack(nums, path, result, used, n):
    if len(path) == n:
        result.append(path)
        return
    else:
        for i in range(n):
            if not used[i]:
                # 第二遍跑重复的 跳过前一个if没用过 
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                # if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue
                else:
                    used[i] = True
                    backtrack(nums, path+[nums[i]], result, used, n)
                    used[i] = False


s = Solution()
print(s.permuteUnique([1,1,2]))
# print(s.permuteUnique([1,1,2]))

