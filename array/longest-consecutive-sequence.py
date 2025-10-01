class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for n in nums:
            if n-1 not in nums:
                len = 1
                while n+1 in nums:
                    len+=1
                    n = n+1
                maxlen = max(len, maxlen)
        return maxlen
