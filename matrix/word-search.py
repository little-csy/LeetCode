class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i:int, j:int, index:int) -> bool:
            if len(word) == index:
                return True
            if i<0 or i>= len(board) or j<0 or j>=len(board[0]) or word[index] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j-1,index+1) or dfs(i,j+1,index+1)
            board[i][j] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        