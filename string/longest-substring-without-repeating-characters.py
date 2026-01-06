class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in last:
                left = last[s[right]]
            last[s[right]] = right
            res = max(res, right-left)
        return res
            