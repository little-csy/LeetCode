from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp = defaultdict(int)
        smp = defaultdict(int)

        for ch in t:
            tmp[ch]+=1
        
        minlen = float('inf')
        start = 0
        l = 0
        require = len(tmp)
        vaild = 0

        for r, c in enumerate(s):
            if c in tmp:
                smp[c]+=1
                if smp[c] == tmp[c]:
                    vaild+=1
            
            while require == vaild:
                if r-l+1<minlen:
                    minlen = r-l+1
                    start = l
                
                if s[l] in tmp:
                    if smp[s[l]] == tmp[s[l]]:
                        vaild -= 1
                    smp[s[l]] -= 1
                l+=1
        
        if minlen == float('inf'):
            return ""
        else:
            return s[start:start+minlen]