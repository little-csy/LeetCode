from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        dir = [(0,1),(0,-1),(-1,0),(1,0)]
        while q and fresh:
            for _ in range(len(q)):
                curx, cury = q.popleft()
                for dirx,diry in dir:
                    nx = curx+dirx
                    ny = cury+diry
                    if nx<0 or nx>=len(grid) or ny<0 or ny>=(len(grid[0])):
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
                        fresh -= 1
            time += 1
        
        if fresh:
            return -1
        else:
            return time   