class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sums = 0
        result = float('inf')
        for j in range(len(nums)):
            sums += nums[j]
            while(sums >= target):
                result = min(result, j-i+1)
                sums -= nums[i]
                i += 1
        
        if result == float('inf'):
            return 0
        else:
            return result
