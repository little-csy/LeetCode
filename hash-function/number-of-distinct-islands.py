class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j , rx, ry, visit, res):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return
            if grid[i][j] == 0 or (i,j) in visit:
                return
            
            visit.add((i,j))
            res.append((i-rx,j-ry))

            dfs(grid, i+1,j,rx,ry,visit,res)
            dfs(grid, i-1,j,rx,ry,visit,res)
            dfs(grid, i,j+1,rx,ry,visit,res)
            dfs(grid, i,j-1,rx,ry,visit,res)
        
        visit = set()
        shape = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visit:
                    res = []
                    dfs(grid, i, j, i, j, visit, res)
                    shape.add(tuple(res))
        return len(shape)