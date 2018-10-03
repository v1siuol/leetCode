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


print(Solution().nextGreatestLetter(["c", "f", "j"], 'a'))
print(Solution().nextGreatestLetter(["c", "f", "j"], 'c'))
print(Solution().nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"n"))
print(Solution().nextGreatestLetter(["e","e","e","k","q","q","q","v","v","y"],"k"))

assert Solution().nextGreatestLetter(["c", "f", "j"], 'a') == 'c'

assert Solution().nextGreatestLetter(["c", "f", "j"], 'c') == 'f'
assert Solution().nextGreatestLetter(["c", "f", "j"], 'd') == 'f'

assert Solution().nextGreatestLetter(["c", "f", "j"], 'f') == 'j'
assert Solution().nextGreatestLetter(["c", "f", "j"], 'g') == 'j'

assert Solution().nextGreatestLetter(["c", "f", "j"], 'j') == 'c'
assert Solution().nextGreatestLetter(["c", "f", "j"], 'k') == 'c'

