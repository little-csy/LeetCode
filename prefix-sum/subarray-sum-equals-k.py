class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0]=1
        pre = 0
        res = 0
        for x in nums:
            pre += x
            if pre-k in mp:
                res += mp[pre-k]
            mp[pre]+=1
        return res