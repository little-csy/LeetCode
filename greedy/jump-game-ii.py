class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        end = 0
        far = 0
        for i in range(len(nums)):
            far = max(far, i+nums[i])
            if i == end and i!= len(nums)-1:
                res +=1
                end = far
        return res