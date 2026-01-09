class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            zero = 0
            for j in range(i,len(nums)):
                if nums[j] == 0:
                    zero += 1
                if zero <=k:
                    res = max(res,j-i+1)
        return res