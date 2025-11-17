class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtracking(l, r, n):
            if l==n and r == n:
                res.append("".join(path))
                return
            if l<n:
                path.append("(")
                backtracking(l+1, r, n)
                path.pop()
            if r<n and r<l:
                path.append(")")
                backtracking(l,r+1,n)
                path.pop()
        
        backtracking(0,0,n)
        return res