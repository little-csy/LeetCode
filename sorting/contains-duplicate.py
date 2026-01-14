from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        if len(cnt) == len(nums):
            return False
        else:
            return True