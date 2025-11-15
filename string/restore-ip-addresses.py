class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def backtracking(s, start):
            if len(path) == 4:
                if start >= len(s):
                    res.append('.'.join(path))
                return
            
            for i in range(start,len(s)):
                seg = s[start:i+1]
                if len(seg) > 1 and seg[0] == '0':
                    continue
                if int(seg) > 255:
                    continue
                path.append(seg)
                backtracking(s, i+1)
                path.pop()
        
        backtracking(s, 0)
        return res