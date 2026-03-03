class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        begin = 0
        for i in range(len(s)):
            l = i-1
            r = i+1

            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            
            if r-l-1>maxlen:
                maxlen = r-l-1
                begin = l+1
            
            l = i
            r = i+1

            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            
            if r-l-1>maxlen:
                maxlen = r-l-1
                begin = l+1
        
        return s[begin:begin+maxlen]