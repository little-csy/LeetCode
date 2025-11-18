class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                return nums[left]
            elif nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
        
        return -1