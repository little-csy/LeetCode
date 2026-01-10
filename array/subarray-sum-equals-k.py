class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0:1}
        sum = 0
        ans = 0
        for num in nums:
            sum += num
            if sum - k in sums: 
                ans += sums[sum - k]
            if sum not in sums:
                sums[sum] = 1
            else:
                sums[sum] = sums[sum]+1
        return ans