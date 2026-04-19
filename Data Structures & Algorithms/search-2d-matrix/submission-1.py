class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        while l < r - 1:
            m = l + (r - l) // 2
            if matrix[m][0] <= target:
                l = m
            else:
                r = m
        
        row = l
        l = 0
        r = len(matrix[row])

        while l < r - 1:
            m = l + (r - l) // 2
            print(f"checking index: [{row}, {m}]")
            print(l)
            print(r)
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                l = m
            else:
                r = m
        return target == matrix[row][l]