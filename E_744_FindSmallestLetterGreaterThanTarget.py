"""
165 / 165 test cases passed.
Status: Accepted
Runtime: 82 ms
"""
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # 2fen
        left = 0
        right = len(letters) - 1
        temp = -1
        mid = (left + right) // 2

        while len(letters) > mid > 0:

            if temp == mid:  # you
                break
            temp = mid
            if target >= letters[mid]:
                left = mid

            elif target < letters[mid]:
                right = mid

            mid = (left + right) // 2

            print(mid)

        if letters[mid] == letters[0] and target < letters[mid]:  # zuo
            return letters[mid]
        elif letters[mid] == letters[len(letters) - 2] and target >= letters[-1]:  # you

            return letters[0]
        else:

            return letters[mid + 1]
