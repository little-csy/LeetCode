import math
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target ==0 :
            return True
        if target>x+y:
            return False

        if target%math.gcd(x,y) == 0:
            return True
        else:
            return False