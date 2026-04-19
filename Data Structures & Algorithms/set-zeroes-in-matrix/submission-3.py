class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        topRowZero = False
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        topRowZero = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if topRowZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        