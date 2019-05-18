"""
Success
Details 
Runtime: 36 ms, faster than 86.84% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 12.9 MB, less than 85.52% of Python3 online submissions for Compare Version Numbers.
"""

class Solution:
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        # 超长度就当0 
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        i = 0
        while i < len(v1):
            if i >= len(v2):
                if v1[i] > 0:
                    return 1
            else:
                if v1[i] > v2[i]:
                    return 1
                elif v1[i] < v2[i]:
                    return -1

            i += 1
        while i < len(v2):
            if v2[i] > 0:
                return -1
            i += 1
        return 0


s = Solution()
print(s.compareVersion('0.1', '1.1') == -1)
print(s.compareVersion('1.0.1', '1') == 1)
print(s.compareVersion('7.5.2.4', '7.5.3') == -1)
print(s.compareVersion('1.01', '1.001') == 0)
print(s.compareVersion('1', '1.1') == -1)

