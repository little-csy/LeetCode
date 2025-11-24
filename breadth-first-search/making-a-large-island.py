class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        hashmap = {0:0}
        n = len(grid)
        id = 2

        def dfs(grid,i,j,id):
            if i<0 or i>=n or j<0 or j>=n or grid[i][j] != 1:
                return 0
            grid[i][j] = id
            area = 1
            area+=dfs(grid,i+1,j,id)
            area+=dfs(grid,i-1,j,id)
            area+=dfs(grid,i,j-1,id)
            area+=dfs(grid,i,j+1,id)
            return area
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    hashmap[id]=dfs(grid,i,j,id)
                    id+=1
        maxarea = max(hashmap.values())
        for i in range(n):
            for j in range(n):
                seen = set()
                if grid[i][j] == 0:
                    cur = 1
                    for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                        nx = i+x
                        ny = j+y
                        if 0<=nx<n and 0<=ny<n and grid[nx][ny] not in seen:
                            seen.add(grid[nx][ny])
                            cur+= hashmap[grid[nx][ny]]
                    maxarea = max(maxarea, cur)
        
        return maxarea
                        
                    