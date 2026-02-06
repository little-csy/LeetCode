class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        l = 0
        maxl = 0
        for r, ch in enumerate(s):
            while s[r] in mp :
                mp.remove(s[l])
                l+=1
            mp.add(ch)
            if r-l+1 > maxl:
                    maxl = r-l+1
        return maxl