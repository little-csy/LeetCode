class Solution:
    def reverse(self, x: int) -> int:
        if x < -1*2**31 or x > 2**31-1:
            return 0
        if x>0:
            flag = 1
        else:
            flag = -1
        re = 0
        absx = abs(x)
        while absx > 0:
            re = re*10 + absx%10
            absx = absx // 10
        
        return flag*re