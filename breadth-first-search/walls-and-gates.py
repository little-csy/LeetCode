from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while q:
            x , y = q.popleft()

            for dx, dy in dirs:
                nx = x+dx
                ny = y+dy

                if 0<=nx<m and 0<=ny<n and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[x][y]+1
                    q.append((nx,ny))