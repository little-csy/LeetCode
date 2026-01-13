class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        sumn = 0
        res = []
        sumn = (1+n)*n//2
        if (sumn-target) %2 == 1:
            return []
        sumneg = (sumn-target)//2
        if sumneg <0 or sumneg > sumn:
            return []
        while sumneg:
            for j in range(n, 0, -1):
                if j<= sumneg:
                    res.append(-j)
                    sumneg -= j
        
        for k in range(1,n+1):
            if -k not in res:
                res.append(k)
        
        return res