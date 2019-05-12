"""
Success
Details 
Runtime: 40 ms, faster than 93.05% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 14.3 MB, less than 5.31% of Python3 online submissions for Longest Consecutive Sequence.
"""

class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        # 看 diss 的
        map_bound2length = dict()
        ret = 0
        for num in nums:
            if num not in map_bound2length:
                left = map_bound2length[num+1] if num+1 in map_bound2length else 0  # add to left
                right = map_bound2length[num-1] if num-1 in map_bound2length else 0
                new_length = left + right + 1  # either 1 (or both in worst case) will be 0
                map_bound2length[num] = new_length
                
                ret = max(ret, new_length)

                map_bound2length[num+left] = new_length
                map_bound2length[num-right] = new_length
                # print(map_bound2length)

        return ret


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([1,2,0,1]))
