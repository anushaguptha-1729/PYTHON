class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = set()

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num = board[i][j]

                        if num != ".":
                            if num in box:
                                return False
                            box.add(num)

        return True
