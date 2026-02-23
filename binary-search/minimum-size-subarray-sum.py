class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        l = 0
        sumc = 0
        for r, c in enumerate(nums):
            sumc += c
            while sumc>=target:
                minlen = min(minlen, r-l+1)
                sumc -= nums[l]
                l+=1
        if minlen == float('inf'):
            return 0
        else:
            return minlen