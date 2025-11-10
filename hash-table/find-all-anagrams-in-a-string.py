from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pmap = Counter(p)
        smap = {}
        need = len(pmap)
        have = 0
        left = 0
        res = []

        for right, val in enumerate(s):
            smap[val] = smap.get(val, 0) + 1

            if val in pmap and smap[val] == pmap[val]:
                have += 1
            
            if right-left+1 == len(p):
                if have == need:
                    res.append(left)
                smap[s[left]] -= 1
                if s[left] in pmap and smap[s[left]] != pmap[s[left]]:
                    have -= 1
                left += 1
        return res