class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        sumn = 0
        res = []
        for i in range(1,n+1):
            sumn+=i
        if (sumn-target) %2 == 1:
            return []
        sumneg = (sumn-target)//2
        while sumneg:
            for j in range(n, 0, -1):
                if j<= sumneg:
                    res.append(-j)
                    sumneg -= j
        
        for k in range(1,n+1):
            if -k not in res:
                res.append(k)
        
        return res