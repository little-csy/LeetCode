class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i,n):
                submin = min(arr[i:j+1])
                ans += submin
        
        return ans
