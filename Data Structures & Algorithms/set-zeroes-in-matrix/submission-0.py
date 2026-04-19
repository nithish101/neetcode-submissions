class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroCols = set()

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0
        