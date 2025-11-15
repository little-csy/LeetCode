class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(nums, start, used):
            res.append(path[:])
            if start >= len(nums):
                return
            
            for i in range(start, len(nums)):
                if i>0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                path.append(nums[i])
                used[i] = 1
                backtracking(nums, i+1, used)
                path.pop()
                used[i] = 0
        
        used = [0]*len(nums)
        nums.sort()
        backtracking(nums, 0, used)
        return res