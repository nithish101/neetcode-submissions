class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        box_sets = [[set() for i in range(3)] for j in range(3)]

        for i in range(len(board)):
            for j in range(len(board)):
                c = board[i][j]
                if board[i][j] == ".":
                    continue
            
                if c in row_sets[i] or c in col_sets[j] or c in box_sets[i // 3][j // 3]:
                    return False

                row_sets[i].add(c)
                col_sets[j].add(c)
                box_sets[i // 3][j // 3].add(c)

        return True