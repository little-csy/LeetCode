class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp = Counter(t)
        require = len(tmp)
        smp = Counter()
        vaild = 0
        start = 0
        minlen = float('inf')
        l = 0

        for r, ch in enumerate(s):
            if ch in tmp:
                smp[ch] += 1
                if smp[ch] == tmp[ch]:
                    vaild += 1
            
            while require == vaild:
                if r-l+1<minlen:
                    minlen = r-l+1
                    start = l

                if s[l] in tmp:
                    if tmp[s[l]] == smp[s[l]]:
                        vaild -= 1
                    smp[s[l]] -= 1
                l+=1

        if minlen == float('inf'):
            return ""
        else:
            return s[start:start+minlen]