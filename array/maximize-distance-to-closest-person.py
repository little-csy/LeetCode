class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        lastp = -1
        res = 0 

        for i in range(n):
            if seats[i] == 1:
                if lastp == -1:
                    res = i
                else:
                    res = max(res, (i-lastp)//2)
                
                lastp = i
        
        res = max(res, n-lastp-1)
        return res