"""
Success
Details 
Runtime: 2404 ms, faster than 5.01% of Python online submissions for Find the Celebrity.
Memory Usage: 12.1 MB, less than 5.12% of Python online submissions for Find the Celebrity.
"""



# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]

graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]

def knows(i, j):
    return graph[i][j]


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = list(range(n))

        know_key = dict()
        dont_know_key = dict()

        while candidate:
            curr = candidate.pop(0)
            dont_know_anyone = True

            for i in range(0, curr):
                if knows(curr, i):
                    dont_know_anyone = False
                    if i not in know_key:
                        know_key[i] = set((curr,))
                    else:
                        know_key[i].add(curr)
                    break
                else:
                    if i not in dont_know_key:
                        dont_know_key[i] = set((curr,))
                    # else:
                    #     dont_know_key[i].add(curr)
            for i in range(curr+1, n):
                if knows(curr, i):
                    dont_know_anyone = False
                    if i not in know_key:
                        know_key[i] = set((curr,))
                    else:
                        know_key[i].add(curr)
                    break
                else:
                    if i not in dont_know_key:
                        dont_know_key[i] = set((curr,))
                    # else:
                    #     dont_know_key[i].add(curr)

            # print(curr, dont_know_anyone, dont_know_key)

            if dont_know_anyone:
                # might be celebrity check n-1 know him 
                if curr not in dont_know_key:
                    # print('?')
                    already_checked = set()
                    if curr in know_key:
                        already_checked = know_key[curr]
                    
                    unchecked = set(range(n)) - already_checked - set((curr,))
                    
                    someone_dont_know_key = False
                    for i in unchecked:
                        if not knows(i, curr):
                            someone_dont_know_key = True
                    if not someone_dont_know_key:
                        return curr
        return -1


print(Solution().findCelebrity(3))

