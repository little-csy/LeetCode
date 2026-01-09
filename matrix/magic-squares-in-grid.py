class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        def isMagic(r,c):
            seen = set()
            if grid[r+1][c+1] != 5:
                return False
            
            for i in range(r, r+3):
                for j in range(c, c+3):
                    v = grid[i][j]
                    if v>9 or v<1 or v in seen:
                        return False
                    seen.add(v)
            
            for k in range(3):
                if grid[r+k][c]+grid[r+k][c+1]+grid[r+k][c+2] != 15:
                    return False
                if grid[r][c+k]+grid[r+1][c+k]+grid[r+2][c+k] != 15:
                    return False
            
            if grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2] != 15:
                return False
            if grid[r+2][c]+grid[r+1][c+1]+grid[r][c+2] != 15:
                return False
            return True


        for r in range(row-2):
            for c in range(col-2):
                if isMagic(r,c):
                    res+=1
        
        return res