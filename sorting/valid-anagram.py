class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0] * 26
        for sch in s:
            cnt[ord(sch)-ord('a')]+=1
        for tch in t:
            cnt[ord(tch)-ord('a')]-=1
        for ch in cnt:
            if ch != 0:
                return False
        return True 