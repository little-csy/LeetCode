class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = set()
        maxlen = 1
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            maxcnt = 1
            num.clear()
            num.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in num:
                    num.add(s[j])
                    maxcnt +=1
                else:
                    break
            maxlen = max(maxlen, maxcnt)
        return maxlen      