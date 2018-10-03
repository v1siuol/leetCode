"""
202 / 202 test cases passed.
Status: Accepted
Runtime: 59 ms
You are here!
Your runtime beats 53.69% of python submissions.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        t1 = []
        i = 0
        while i < len(nums):
            v =nums[i]
            if nums[i] > 0:
                while i+1 < len(nums) and nums[i+1] > 0:
                    i += 1
                    v += nums[i]
                t1.append(v)
            elif nums[i] < 0:
                while i+1 < len(nums) and nums[i+1] < 0:
                    i += 1
                    v += nums[i]
                t1.append(v)
            i += 1
        #print(t1)
        if len(t1) == 1 and t1[0] < 0:
            return max(nums)
        i = 0
        pt = 0
        nt = 0
        re = []

        while i < len(t1):
            if t1[i] < 0:
                if t1[i] + pt <= 0:
                    re.append(pt)
                    pt = 0
                    nt = 0
                else:
                    nt += t1[i]

                    #nt += t1[i]
            else:
                if t1[i] + nt > 0:
                    #print("?")
                    #print(i, nt)
                    pt += (t1[i] + nt)
                    nt = 0

                else:
                    re.append(pt)
                    pt = pt + t1[i] + nt
                    nt = 0
            #print(i, pt, re, nt)
            i += 1
        re.append(pt)
        return max(re)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
#print(Solution().maxSubArray([-1]))  # -1
print(Solution().maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))  # 6
print(Solution().maxSubArray([-3,1,0,-1,-2,3,2,-1]))  # 5
print(Solution().maxSubArray([2,-3,1,3,-3,2,2,1]))  # 6
print(Solution().maxSubArray([0,0,3,3,0,-2,3,-2,-1,-1,2,1]))  # 7
print(Solution().maxSubArray([-9,-6,2,-5,-8,1,6,9,-8,0,5,5,    -4,7,4,1,7,-3,-1]))  # 33
print(Solution().maxSubArray([1,-3,2,0,-1,0,-2,-3,1,2,-3,2]))  # 3
print(Solution().maxSubArray([-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7]))  # 33
