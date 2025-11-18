class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        def dfs(board, word, index, x, y):
            if board[x][y] != word[index]:
                return False
            if len(word)-1 == index:
                return True
            
            temp = board[x][y]
            board[x][y] = '#'
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]) or board[nx][ny] == '#':
                    continue
                if (dfs(board,word,index+1,nx,ny)):
                    return True
            board[x][y] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, 0, i, j):
                    return True
        return False