class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        best = ""

        for i in range(n):
            for j in range(i+1,n):
                length = 0
                while i+length < n and j+length < n and s[i+length] == s[j+length]:
                    length += 1
                if length > len(best):
                    best = s[i:i+length]
        
        return best
