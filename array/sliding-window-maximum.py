class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if k == 1:
            return nums
        else:
            for i in range(len(nums)-k+1):
                window_max = nums[i]
                for j in range(i+1, i+k):
                    if nums[j] > window_max:
                        window_max = nums[j]
                result.append(window_max)
            
            return result
        