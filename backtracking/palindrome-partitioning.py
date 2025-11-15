class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def backtracking(s, start):
            if start >= len(s):
                res.append(path[:])
                return

            for i in range(start,len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    path.append(s[start:i+1])
                else:
                    continue
                backtracking(s, i+1)
                path.pop()
        
        backtracking(s, 0)
        return res