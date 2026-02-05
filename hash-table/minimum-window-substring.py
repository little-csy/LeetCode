from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp = Counter(t)
        smp = Counter()
        require = len(tmp)
        vaild = 0
        l = 0
        start = 0
        slen = float('inf')

        for r, ch in enumerate(s):
            if ch in tmp:
                smp[ch] += 1
                if smp[ch] == tmp[ch]:
                    vaild +=1
            
            while vaild == require:
                if r-l+1<slen:
                    slen = r-l+1
                    start = l
                
                if s[l] in tmp:
                    if smp[s[l]] == tmp[s[l]]:
                        vaild -= 1
                    smp[s[l]] -= 1
                l+=1
        
        if slen == float('inf'):
            return ""
        else:
            return s[start:start+slen+1]