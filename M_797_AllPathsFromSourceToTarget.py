"""
Author  => v1siuol
Date    => 2018.06.01
26 / 26 test cases passed.
Status: Accepted
Runtime: 362 ms
You are here! 
Your runtime beats 20.21 % of python submissions.
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        curr_path = [0]
        result =[]
        curr_s = [graph[0]][:]
        n = len(graph[:])

        while curr_s:
            while not curr_s[-1]:
                curr_s.pop()
                curr_path.pop(-1)
                if not curr_s:
                    return result


            temp = curr_s[-1].pop()
            curr_path.append(temp)
            # print(temp, curr_path, curr_s, graph[temp])
            if graph[temp][:]:
                curr_s.append(graph[temp][:])  #wth
            else:
                if temp == n - 1:
                    result.append(curr_path[:])
                curr_path.pop(-1)

        return result

print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))