class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = [[False]*n for _ in range(m)]
        shapes = set()

        def dfs(i,j,rx,ry,res):

            if i<0 or i>=m or j<0 or j>=n:
                return
            
            if grid[i][j] == 0 or visit[i][j]:
                return
            
            visit[i][j] = True

            res.append((i-rx,j-ry))

            dfs(i-1,j,rx,ry,res)
            dfs(i+1,j,rx,ry,res)
            dfs(i,j-1,rx,ry,res)
            dfs(i,j+1,rx,ry,res)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visit[i][j]:
                    res = []
                    dfs(i,j,i,j,res)
                    shapes.add(tuple(res))
        return len(shapes)            
