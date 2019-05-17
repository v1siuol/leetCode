"""
Success
Details 
Runtime: 172 ms, faster than 60.58% of Python3 online submissions for Strobogrammatic Number II.
Memory Usage: 20.2 MB, less than 22.51% of Python3 online submissions for Strobogrammatic Number II.
"""
class Solution:
    def findStrobogrammatic(self, n: 'int') -> 'List[str]':
        # 没有0 也可以中间展开 
        single_layer = ['0', '1', '8']
        double_layer_frt = ['11', '88', '69', '96']
        double_layer_exp = ['00', '11', '88', '69', '96']

        if n == 1:
            return single_layer
        i = 1
        ret = double_layer_frt[:]

        while i < n // 2:
            next_layer = []
            for term in ret:
                next_layer += [term[:i] + ele + term[-i:] for ele in double_layer_exp]
                
            ret = next_layer
            i += 1

        if n % 2 == 1:
            next_layer = []
            for term in ret:
                next_layer += [term[:i] + ele + term[-i:] for ele in single_layer]
            ret = next_layer

        return ret


s = Solution()
# print(s.findStrobogrammatic(1))
# print(s.findStrobogrammatic(2))
# print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))

