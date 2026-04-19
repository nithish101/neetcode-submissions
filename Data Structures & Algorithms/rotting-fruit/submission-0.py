class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while fresh > 0 and len(q) > 0:
            l = len(q)
            for i in range(l):
                x, y = q.popleft()
                for dx, dy in dirs:
                    if (
                        0 <= x + dx < len(grid)
                        and 0 <= y + dy < len(grid[x + dx])
                        and grid[x + dx][y + dy] == 1
                    ):
                        grid[x + dx][y + dy] = 2
                        fresh -= 1
                        q.append((x + dx, y + dy))
            time += 1

        return time if fresh == 0 else -1