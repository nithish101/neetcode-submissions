class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, visited):
            if (i, j) in visited:
                return False
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
            if board[i][j] == word[len(visited)]:
                
                visited.add((i, j))
                if len(visited) == len(word):
                    return True
                found = (dfs(i - 1, j, visited) or
                        dfs(i + 1, j, visited) or
                        dfs(i, j - 1, visited) or
                        dfs(i, j + 1, visited))
                visited.remove((i, j))
                return found

        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, visited):
                        return True
        return False

        
                
