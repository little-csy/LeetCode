class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hp = set(nums)
        maxlen = 0
        for x in nums:
            if x-1 not in hp:
                length = 1
                while x+1 in nums:
                    length += 1
                    x+=1
                maxlen = max(maxlen,length)
        return maxlen