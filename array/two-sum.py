class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = dict()
        for index, value in enumerate(nums):
            need = target - value
            if need in cnt:
                return [cnt[need], index]
            cnt[value] = index
        return []