class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row+1) for _ in range(query_row+1)]
        dp[0][0] = poured

        for r in range(query_row):
            for c in range(r+1):
                extra = max(0, dp[r][c]-1)
                if extra:
                    dp[r+1][c] += extra/2
                    dp[r+1][c+1] += extra/2
        
        return min(1, dp[query_row][query_glass])
        