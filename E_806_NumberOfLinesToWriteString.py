"""
Author  => v1siuol
Date    => 2018.05.13
26 / 26 test cases passed.
Status: Accepted
Runtime: 36 ms
You are here! 
Your runtime beats 99.61 % of python3 submissions.
"""
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        base = 97
        limit = 100
        curr = 0

        rline = 1
        rwidth = 0
        for char in S:
            rwidth += widths[ord(char)-base]

            if rwidth > limit:
                rline += 1
                rwidth = widths[ord(char)-base]
            # print(char)
            # print(widths[ord(char)-base])

        return [rline, rwidth]
        
        
print(Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))
