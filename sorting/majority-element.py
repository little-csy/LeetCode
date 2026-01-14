from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mtime = len(nums)//2

        hp = Counter(nums)

        for val, freq in hp.items():
            if freq > mtime:
                return val
