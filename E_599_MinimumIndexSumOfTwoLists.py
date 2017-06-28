"""
133 / 133 test cases passed.
Status: Accepted
Runtime: 515 ms
You are here!
Your runtime beats 24.04 % of python submissions.
"""
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        #print(list1.index("Shogus"))
        i = 0
        first = True
        result = []
        while i < len(list1):
            try:
                ex = list2.index(list1[i])
            except ValueError:
                ex = -1
            if ex != -1:
                if first:
                    min = i + ex
                    result.append(list1[i])
                    first = False
                else:
                    if i + ex < min:
                        result = []
                        result.append(list1[i])
                    elif i + ex == min:
                        result.append(list1[i])
            i += 1
        return result

print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
