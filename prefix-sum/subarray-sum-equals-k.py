class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        cnt = 0
        presum = 0
        for nums in nums:
            presum += nums
            if presum-k in hashmap:
                cnt += 1
            hashmap[presum] = hashmap.get(presum, 0) + 1
        return cnt