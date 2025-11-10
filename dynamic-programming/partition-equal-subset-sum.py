class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        else:
            target = sum(nums)//2
            l = len(nums)
            dp = [0] * (target+1)
            for i in range(l):
                for j in range(target, nums[i]-1, -1):
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
            
            if dp[target] == target:
                return True
            else:
                return False