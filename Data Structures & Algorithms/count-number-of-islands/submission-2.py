class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        totalIslands = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y):
            nonlocal visited
            if (x, y) in visited:
                return
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
                return
            visited.add((x, y))
            if (grid[x][y] == "1"):
                for dx, dy in dirs:
                    dfs(x + dx, y + dy)
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    totalIslands += 1
                    dfs(i, j)

        return totalIslands
