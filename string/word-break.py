class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for j in range(1, len(s)+1):
            for i in range(0,j):
                sub = s[i: j]
                if sub in wordDict and dp[i] == True:
                    dp[j] = True
        
        return dp[len(s)]