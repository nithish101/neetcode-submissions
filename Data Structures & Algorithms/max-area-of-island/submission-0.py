class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def findIsland(i, j) -> int:
            if (
                i < 0 or j < 0
                or i >= len(grid)
                or j >= len(grid[i])
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return 0
            visited.add((i, j))
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            total = 0
            for dx, dy in dirs:
                total += findIsland(i + dx, j + dy)
            return 1 + total

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans = max(ans, findIsland(i, j))

        return ans
                