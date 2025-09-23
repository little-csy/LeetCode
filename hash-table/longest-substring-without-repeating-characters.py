class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = set()
        left = 0
        maxlen = 0
        for right in range(len(s)):
            while s[right] in num:
                num.remove(s[left])
                left += 1
            num.add(s[right])
            maxlen = max(maxlen, right-left+1)
        return maxlen