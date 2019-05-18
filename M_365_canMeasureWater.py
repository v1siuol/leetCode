class Solution:
    def canMeasureWater(self, x: 'int', y: 'int', z: 'int') -> 'bool':
        # 慌 了  
        if x + y < z:
            return False

        if x == z or y == z or x + y == z:
            return False

        return z % gcd(x, y) == 0





def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


s = Solution()
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(2, 6, 5))
