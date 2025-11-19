class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n//2
        countY = [0,0,0]
        ncountY = [0,0,0]

        for i in range(n):
            for j in range(n):
                isY = (
                    (i<=mid and i==j)or
                    (i<=mid and i==n-j-1)or
                    (i>mid and j==mid)
                )
                if isY:
                    countY[grid[i][j]]+=1
                else:
                    ncountY[grid[i][j]]+=1
        
        totaly = sum(countY)
        ntotaly = sum(ncountY)
        res = float('inf')
        for c1 in range(3):
            for c2 in range(3):
                if c1 == c2:
                    continue
                turny = totaly-countY[c1]
                nturny = ntotaly-ncountY[c2]
                res = min(res, turny+nturny)

        return res
                