class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        results = [0] * len(nums)
        k = len(nums) -1

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            if left_sq >= right_sq:
               results[k] = left_sq
               left += 1
            else:
                results[k] = right_sq
                right -= 1
            k -= 1

        return results
