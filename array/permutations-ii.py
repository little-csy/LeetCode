class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i >0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking(nums, used)
                used[i] = 0
                path.pop()
        
        used = [0] * len(nums)
        backtracking(nums, used)
        return res