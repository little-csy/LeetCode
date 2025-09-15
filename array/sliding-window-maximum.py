class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) == 1:
            return [nums[0]]
        elif len(nums) == 2:
            if k > 1:
                return [max(nums[0], nums[1])]
            else:
                return [nums[0], nums[1]]
        else:
            for i in range(len(nums)-2):
                window_max = nums[i]
                for j in range(i+1, i+k):
                    if nums[j] > window_max:
                        window_max = nums[j]
                result.append(window_max)
            
            return result
        