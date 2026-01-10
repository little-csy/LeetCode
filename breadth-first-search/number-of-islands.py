class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        def dfs(grid, i, j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j] == "0":
                return False
            grid[i][j] = "0"
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            return True
        
        for i in range(row):
            for j in range(col):
                if dfs(grid, i, j):
                    res+=1
        return res
