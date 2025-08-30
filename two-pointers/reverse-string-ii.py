class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            if i+k <= len(s):
                s[i:i+k] = s[i:i+k][::-1]
                continue
            s[i:] = s[i:][::-1]
        
        return "".join(s)