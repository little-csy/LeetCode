class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = 0
        start = 0
        for i in range(n):
            l = i-1
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>maxlen:
                maxlen = r-l-1
                start = l+1
            l = i
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>maxlen:
                maxlen = r-l-1
                start = l+1
        return s[start:start+maxlen]
                
