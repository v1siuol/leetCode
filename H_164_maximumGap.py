"""
Success
Details 
Runtime: 56 ms, faster than 38.93% of Python3 online submissions for Maximum Gap.
Memory Usage: 14.2 MB, less than 7.14% of Python3 online submissions for Maximum Gap.
"""
class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return 0
        maximum = max(nums)
        minimum = min(nums)

        bucket_cap = max(1, (maximum-minimum)// (len(nums)-1))
        bucket_size = (maximum-minimum) // bucket_cap + 1

        bucket_max = [float('-inf') for _ in range(bucket_size)]
        bucket_min = [float('inf') for _ in range(bucket_size)]

        for num in nums:
            idx = (num-minimum) // bucket_cap
            # print(idx, bucket_size)
            bucket_max[idx] = max(bucket_max[idx], num)
            bucket_min[idx] = min(bucket_min[idx], num)

        ret = 0
        prev_max = minimum
        for i in range(bucket_size):
            if bucket_min[i] == float('inf') or bucket_max[i] == float('-inf'):
                continue  # empty bucket

            ret = max(ret, bucket_min[i]-prev_max)
            prev_max = bucket_max[i]

        return ret


s = Solution()
# print(s.maximumGap([3,6,9,1]))
# print(s.maximumGap([10]))
print(s.maximumGap([1,10000000]))

