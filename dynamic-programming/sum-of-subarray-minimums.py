class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            curr_min = arr[i]
            for j in range(i,n):
                curr_min = min(curr_min, arr[j])
                ans += curr_min
        
        return ans
