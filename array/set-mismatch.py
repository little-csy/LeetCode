class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dump = 0

        for val in nums:
            if val in seen:
                dump = val
            seen.add(val)
        
        missing = 0
        for num in range(1, len(nums)+1):
            if num not in seen:
                missing = num
                break
        
        return [dump, missing]