class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l = 0
        hp = set()
        for r, val in enumerate(s):
            while val in hp:
                hp.remove(s[l])
                l+=1
            hp.add(val)
            if r-l+1>maxlen:
                maxlen = r-l+1
        return maxlen
