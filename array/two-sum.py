from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = defaultdict(int)
        for idx, val in enumerate(nums):
            need = target-val
            if need in hp:
                return [hp[need], idx]
            hp[val] = idx
            
        