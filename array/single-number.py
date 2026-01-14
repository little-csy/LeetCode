from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hp = Counter(nums)
        for x, freq in hp.items():
            if freq == 1:
                return x