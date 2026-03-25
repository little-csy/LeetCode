class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        res = []
        tire = {}
        for word in words:
            node = tire
            for w in word:
                node = node.setdefault(w, {})
            node['#'] = word
        
        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return
            
            node = node[c]

            if '#' in node:
                res.append(node['#'])
                node.pop('#')
            
            board[i][j] = '#'

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+dx, j+dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, node)
            
            board[i][j] = c
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,tire)

        return res