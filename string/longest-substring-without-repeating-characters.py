class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        l = 0
        maxl = 0
        for r, ch in enumerate(s):
            while s[r] in mp :
                if r-l > maxl:
                    maxl = r-l
                mp.remove(s[l])
                l+=1
            mp.add(ch)
        return maxl