class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            cnt = [0]*26
            for ch in s:
                cnt[ord(ch)-ord('a')]+=1
            
            group[tuple(cnt)].append(s)
        
        return list(group.values())