class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minp = float('inf')
        maxp = 0
        for p in prices:
            if p<minp:
                minp = p
            else:
                maxp = max(maxp, p-minp)
        return maxp