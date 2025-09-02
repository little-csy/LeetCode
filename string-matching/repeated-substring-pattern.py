class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        next = [0] * len(s)
        self.getNext(s, next)
        if next[-1]!=0:
            repeat = len(s)-next[-1]
            if len(s) % repeat == 0:
                return True
        return False
        
    def getNext(self, s:str, next:List[int]) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j>0 and s[i]!=s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j +=1
            next[i] = j