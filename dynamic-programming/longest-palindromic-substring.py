class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0]*n
        center = 0
        right = 0
        max_len = 0
        max_center = 0

        for i in range(n):
            mirror = 2*center - i

            if i<right:
                p[i] = min(p[mirror], right-i)
            
            while i-p[i]-1>=0 and i+p[i]+1<n and t[i-p[i]-1] == t[i+p[i]+1]:
                p[i]+=1
            
            if i+p[i]>right:
                right = i+p[i]
                center = i
            
            if p[i]>max_len:
                max_center = i
                max_len = p[i]
        
        start = (max_center-max_len)//2

        return s[start:start+max_len]