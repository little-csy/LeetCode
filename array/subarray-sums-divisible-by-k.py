class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = {0:1}
        pre = 0
        res = 0

        for x in nums:
            pre += x
            mod = pre%k
            if mod in cnt:
                res += cnt[mod]
            cnt[mod] = cnt.get(mod,0)+1
        return res
