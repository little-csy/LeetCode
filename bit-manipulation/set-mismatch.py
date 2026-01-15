class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen  = set()
        for val in nums:
            if val in seen:
                return [val, val+1]
            seen.add(val)