class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        county = [0,0,0]
        countny = [0,0,0]
        n = len(grid)
        mid = n//2

        for i in range(n):
            for j in range(n):
                if (i<=mid and i==j) or (i<=mid and i == n-j-1) or (i>mid and j==mid):
                    isY = True
                else:
                    isY = False
                
                if isY:
                    county[grid[i][j]] += 1
                else:
                    countny[grid[i][j]] += 1
        
        totaly = sum(county)
        totalny = sum(countny)
        res = float('inf')

        for c1 in range(3):
            for c2 in range(3):
                if c1 == c2:
                    continue
                turny = totaly - county[c1]
                turnny = totalny - countny[c2]

                res = min(res, turny+turnny)
        
        return res