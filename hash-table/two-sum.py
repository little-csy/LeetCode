class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = dict()
        for index, value in enumerate(nums):
            need = target - value
            if need in cnt:
                return [index, cnt[need]]
            else:
                cnt[value] = index
        
        return []