class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = float('-inf')
        for i in range(len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            maxsum = max(maxsum, cursum)
        return maxsum