class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsort = sorted(nums)
        left = len(nums)
        right = 0

        for i in range(len(nums)):
            if nums[i] != numsort[i]:
                left = min(left,i)
                right = max(right,i)
        
        if right<left:
            return 0
        else:
            return right-left+1
