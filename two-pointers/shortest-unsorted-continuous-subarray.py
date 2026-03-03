class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxseen = float('-inf')
        right = -1

        minseen = float('inf')
        left = -1

        for i in range(n):
            if nums[i]<maxseen:
                right = i
            else:
                maxseen = nums[i]
        
        for j in range(n-1,-1,-1):
            if nums[j]>minseen:
                left = j
            else:
                minseen = nums[j]
        
        if right == -1:
            return 0
        else:
            return right-left+1