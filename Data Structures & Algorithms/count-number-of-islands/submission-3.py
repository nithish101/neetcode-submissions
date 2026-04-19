class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        def dfs(i, j):
            if (
                (i, j) in visited
                or i < 0 or i >= len(grid)
                or j < 0 or j >= len(grid[i])
                or grid[i][j] == "0"
            ):
                return
            dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            visited.add((i, j))
            for dx, dy in dirs:
                dfs(i + dx, j + dy)
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res