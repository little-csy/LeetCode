class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minp = float('inf')
        for p in prices:
            minp = min(minp, p)
            res = max(res,p-minp)
        return res