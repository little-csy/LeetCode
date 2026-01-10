class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtracking(l, r):
            if len(path) == 2*n:
                res.append(''.join(path))
            
            if l<n:
                path.append('(')
                backtracking(l+1,r)
                path.pop()
            if r<l:
                path.append(')')
                backtracking(l, r+1)
                path.pop()
        
        backtracking(0,0)
        return res