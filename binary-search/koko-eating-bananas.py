class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<=r:
            hour = 0
            k = (l+r)//2

            for p in piles:
                if p%k == 0:
                    hour+=p//k
                else:
                    hour+=p//k+1
            
            if hour<=h:
                r = k-1
            else:
                l = k+1
        
        return l