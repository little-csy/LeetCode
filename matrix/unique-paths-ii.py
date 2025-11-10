class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        i = 0
        j = 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        while i < m:
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
                i += 1
            else:
                break
        while j < n:
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
                j += 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 0
        
        return dp[m-1][n-1]