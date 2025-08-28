class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()
        total = self.get_total(n)

        while total != 1:
            s.add(total)
            total = self.get_total(total)
            if total in s:
                return False
        
        return True

    def get_total(self, n: int) -> int:
        total = 0
        while n != 0 :
            num = n % 10
            total += num * num
            n //= 10
        
        return total