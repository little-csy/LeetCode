from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            c, t = cost[i], time[i]
            for j in range(n, 0, -1):
                prev = max(0, j - 1 - t)
                dp[j] = min(dp[j], dp[prev] + c)

        return dp[n]