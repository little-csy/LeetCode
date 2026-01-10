class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        pre = 0
        for n in nums:
            pre += n
            if pre-k in mp:
                res+=mp[pre-k]
            mp[pre] += 1
        return res