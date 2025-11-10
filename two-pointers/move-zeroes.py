class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1