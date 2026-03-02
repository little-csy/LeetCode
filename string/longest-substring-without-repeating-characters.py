class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        mp = set()

        for r, ch in enumerate(s):
            while ch in mp:
                mp.remove(s[l])
                l+=1
            
            mp.add(ch)

            if r-l+1>maxl:
                maxl = r-l+1
        
        return maxl