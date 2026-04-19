class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0

        def dfs(i, j):
            print(i, j)
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                total += 1
                dfs(i, j)
            
        return total
        
        
