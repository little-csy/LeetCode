class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            res = 0
            for j in range(i, n):
                res += nums[j]
                if res == k:
                    ans+=1
        return ans