from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        smap = {}
        left = 0
        need = len(tmap)
        have = 0
        res = [-1, -1]
        reslen = float('inf')
        for right, val in enumerate(s):
            smap[val] = smap.get(val, 0) + 1

            if val in tmap and smap[val] == tmap[val]:
                have += 1
            
            while have == need:
                if right - left + 1 < reslen:
                    res = [left, right]
                    reslen = right -left + 1
                
                smap[s[left]] -= 1
                if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                    have -= 1
                left += 1
            
        l , r = res
        if reslen == float('inf'):
            return ""
        else:
            return s[l:r+1]