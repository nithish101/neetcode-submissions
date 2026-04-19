class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]
        for r in range(m - 1):
            newrow = [row[0]]
            for j in range(1, n):
                newrow.append(row[j] + newrow[-1])
            row = newrow
        return row[-1]