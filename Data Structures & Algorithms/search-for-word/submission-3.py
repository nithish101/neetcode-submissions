class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, letter):
            if (i < 0 or i >= len(board)
                or j < 0 or j >= len(board[i])
                or board[i][j] == "*"
                or letter >= len(word)):
                return False
            if board[i][j] != word[letter]:
                return False
            if letter == len(word) - 1:
                return True
            board[i][j] = "*"
            res = (
                dfs(i - 1, j, letter + 1)
                or dfs(i + 1, j, letter + 1)
                or dfs(i, j - 1, letter + 1)
                or dfs(i, j + 1, letter + 1)
            )
            board[i][j] = word[letter]
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        return False