class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []
        word_set = set(words)  # 为了避免重复word输入

        def dfs(i, j, k, word):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'     # 标记访问

            found = (dfs(i+1, j, k+1, word) or
                     dfs(i-1, j, k+1, word) or
                     dfs(i, j+1, k+1, word) or
                     dfs(i, j-1, k+1, word))

            board[i][j] = temp    # 回溯
            return found

        for word in word_set:
            found_word = False
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, 0, word):
                        res.append(word)
                        found_word = True
                        break
                if found_word:
                    break
        return res
