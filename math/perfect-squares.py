class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        square = []
        for i in range(1, int(n**0.5)+1):
            square.append(i*i)
        
        for i in range(len(square)):
            for j in range(square[i], n+1):
                dp[j] = min(dp[j], dp[j- square[i]] +1)
        return dp[n]