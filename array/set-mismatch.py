class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen  = set()
        for val in nums:
            if val in seen:
                if val == 2 and 1 not in seen:
                    return [val, val+1]
                else:
                    return [val, val+1]
            seen.add(val)