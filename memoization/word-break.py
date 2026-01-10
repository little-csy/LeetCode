class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        def dfs(start):
            if start == len(s):
                return True
            
            for i in range(start+1,len(s)+1):
                if s[start:i] in wordSet:
                    if dfs(i):
                        return True
            return False
        
        return dfs(0)