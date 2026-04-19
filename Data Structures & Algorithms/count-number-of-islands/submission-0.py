class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == "1":
                    count += 1
                    self.visitIsland(i, j, visited, grid)
        return count

    def visitIsland(self, i, j, visited, grid):
        if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
            return
        if (i, j) in visited:
            return
        visited.add((i, j))
        if grid[i][j] == "1":
            self.visitIsland(i + 1, j, visited, grid)
            self.visitIsland(i, j + 1, visited, grid)
            self.visitIsland(i - 1, j, visited, grid)
            self.visitIsland(i, j - 1, visited, grid)