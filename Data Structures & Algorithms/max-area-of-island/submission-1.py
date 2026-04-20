class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sol = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if (i < 0 or i >= len(grid)
            or j < 0 or j >= len(grid[i])
            or grid[i][j] == 0):
                return 0

            grid[i][j] = 0
            size = 1
            for dx, dy in dirs:
                size += dfs(i + dx, j + dy)
            return size

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                sol = max(sol, dfs(i, j))

        return sol