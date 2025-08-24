class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx, starty, offset, count = 0, 0, 1, 1
        List = [[0] * n for _ in range(n)]
        Loop = n//2
        while(Loop > 0):
            for j in range(starty, n - offset):
                List[startx][j] = count
                count += 1
                j += 1
            for i in range(startx, n - offset):
                List[i][j] = count
                count += 1
                i += 1
            for j in range(j, starty, -1):
                List[i][j] = count
                count += 1
                j += 1
            for i in range(i, startx, -1):
                List[i][starty] = count
                count += 1
                i += 1
            startx +=1
            starty +=1
            offset +=1
            Loop -=1
        if n % 2 == 1:
            List[n//2][n//2] = count
        return List