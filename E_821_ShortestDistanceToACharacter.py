"""
Author  => v1siuol
Date    => 2018.05.13
76 / 76 test cases passed.
Status: Accepted
Runtime: 48 ms
"""
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        count = 0
        rarr = []
        index = 0
        isOne = False

        while index < len(S):
            if C == S[index]:
                if count >= 0:        
                    rarr.extend(list(range(count, -1, -1)))
                    count = 0
                    break
            else:
                count += 1
            index += 1


        index += 1
        while index < len(S):
            if C == S[index]:
                if count & 1 == 1:
                    mid = count // 2 + 1
                    isOne = True
                    
                else :
                    mid = count // 2
                    isOne = False
                rarr.extend(self.shelper(mid, isOne))
                # print(isOne)
                rarr.append(0)
                count = 0
            else:
                count += 1
            # print(count, S[index])

            index += 1


        rarr.extend(list(range(1,count+1)))
            
        return rarr

    def shelper(self, num, isOne):
        if num <= 0:
            return []
        temp = list(range(1, num))
        if not isOne:
            temp.append(num)
        temp.extend(list(range(num, 0, -1)))

        return temp
       
print(Solution().shelper(0, False))
print(Solution().shortestToChar("aaba", 'b'))
print(Solution().shortestToChar("loveleetcode", 'e'))
