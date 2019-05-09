"""
Success
Details 
Runtime: 44 ms, faster than 46.43% of Python online submissions for Gas Station.
Memory Usage: 12.6 MB, less than 5.47% of Python online submissions for Gas Station.
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        curr_gas = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start = i + 1
                curr_gas = 0

        if total_gas < 0:
            return -1
        else:
            return start 


s = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas, cost))

gas  = [1,2,3,4,5]
cost = [3,4,6,1,2]
print(s.canCompleteCircuit(gas, cost))


gas  = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))
