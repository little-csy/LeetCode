class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        