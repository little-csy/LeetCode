class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        def get_total(n):
            total = 0
            while n>0:
                digital = n%10
                total += digital*digital
                n = n//10
            return total
        
        while True:
            n = get_total(n)
            if n not in s:
                s.add(n)
            else:
                return False
            if n==1:
                return True