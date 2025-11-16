class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ['.'*n for _ in range(n)]
        col = set()
        diag1 = set()
        diag2 = set()

        def backtracking(board, r, n):
            if r == n:
                res.append(board[:])
                return
            for c in range(n):
                if c in col or r-c in diag1 or r+c in diag2:
                    continue
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                row = list(board[r])
                row[c] = 'Q'
                board[r] = ''.join(row)
                backtracking(board, r+1, n)
                row = list(board[r])
                row[c] = '.'
                board[r] = ''.join(row)
                col.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
        
        backtracking(board, 0, n)
        return res