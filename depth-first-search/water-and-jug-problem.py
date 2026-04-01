class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target ==0 :
            return True
        if target>x+y:
            return False
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        maxgcd = gcd(x,y)
        if target%maxgcd == 0:
            return True
        else:
            return False