import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for x in nums:
            idx = bisect.bisect_left(tail,x)
            if idx == len(tail):
                tail.append(x)
            else:
                tail[idx] = x
        return len(tail)
        