class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n-1):
            res = []
            i = 0
            while i < len(s):
                cnt = 1
                for j in range(i+1, len(s)):
                    if s[j] == s[i]:
                        cnt += 1
                    else:
                        break
                
                res.append(str(cnt))
                res.append(s[i])
                i+=cnt
            s = ''.join(res)
        
        return s