class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        def dfs(grid, i, j):
            grid[i][j] = '0'
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]) or grid[nx][ny] == '0':
                    continue
                dfs(grid,nx,ny)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res +=1
        return res