from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pmap = Counter(p)
        smap = Counter()
        k = len(p)

        for i, val in enumerate(s):
            smap[val]+=1

            if i>=k:
                smap[s[i-k]]-=1
                if smap[s[i-k]] == 0:
                    del smap[s[i-k]]
            
            if pmap == smap:
                res.append(i-k+1)
        return res