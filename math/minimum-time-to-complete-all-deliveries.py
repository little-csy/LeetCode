class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        l = 1
        r = 4*10**9

        while l<=r:
            mid = (l+r)//2
            
            ok = True

            if mid - mid//r1<d1:
                ok = False
            
            if mid-mid//r2<d2:
                ok = False
            
            if mid-mid//math.lcm(r1,r2)<d1+d2:
                ok = False
            
            if ok==True:
                r = mid -1
            else:
                l = mid+1
        return l        