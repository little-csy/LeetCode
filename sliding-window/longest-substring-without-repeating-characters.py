class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in last and left<=last[s[right]]:
                left = last[s[right]]+1
            last[s[right]] = right
            res = max(res, right-left+1)
        return res
            