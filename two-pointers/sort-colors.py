class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num0 = 0
        num1 = 0
        num2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num0+=1
            elif nums[i] == 1:
                num1+=1
            else:
                num2+=1
        
        for j in range(num0):
            nums[j] = 0
        
        for k in range(num0, num0+num1):
            nums[k] = 1
        
        for m in range(num0+num1, len(nums)):
            nums[m] = 2