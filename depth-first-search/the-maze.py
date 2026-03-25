from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        q = deque()
        visit = set()
        q.append(tuple(start))
        visit.add(tuple(start))

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            x,y = q.popleft()

            if (x,y) == tuple(destination):
                return True

            for dx,dy in dirs:
                nx = x
                ny = y
                while 0<=nx+dx<m and 0<=ny+dy<n and maze[nx+dx][ny+dy] == 0:
                    nx+=dx
                    ny+=dy
                if (nx,ny) not in visit:
                    visit.add((nx,ny))
                    q.append((nx,ny))
        return False