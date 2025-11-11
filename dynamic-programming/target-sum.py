#left+ right = sum
#left - right = target
#left+left-target = sum
#left = (target+sum)//2
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total+target) % 2 == 1:
            return 0
        else:
            left = (total+target)//2
            dp = [0] * (left+1)
            dp[0] = 1
            for i in range(len(nums)):
                for j in range(left, nums[i]-1, -1):
                    dp[j] += dp[j-nums[i]]
            
            return dp[left]
        