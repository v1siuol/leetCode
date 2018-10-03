"""
200 / 200 test cases passed.
Status: Accepted
Runtime: 49 ms
You are here!
Your runtime beats 77.91% of python submissions.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        re = 0
        i = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices):
                n = prices[j] - prices[i]
                if re < n:
                    re = n
                j += 1
            i += 1
        return re
        """

# 一步一步走 边搜 双指针判断
        if prices:
            mi = prices[0]
            ma = prices[0]
            temp = prices[0]
            isMin = False
            i = 1
            while i < len(prices):
                v = prices[i]
                if isMin and v - temp > ma - mi:
                    ma = v
                    mi = temp
                    temo = False
                if v > ma:
                    ma = v
                elif v < mi and v < temp:
                    temp = v
                    isMin = True
                i += 1
                #print(ma, mi, temp)
            return ma - mi
        return 0

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([4,7,1,2,11]))
