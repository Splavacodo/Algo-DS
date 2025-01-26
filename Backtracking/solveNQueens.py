class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        boards = []
        curr_board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()
        neg_diag = set()
        
        def find_solutions(row):
            if row == n:
                flattened_board = ["".join(row) for row in curr_board]
                boards.append(flattened_board)
                return
            
            for col in range(n):
                if col in cols or row + col in pos_diag or row - col in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                curr_board[row][col] = "Q"

                find_solutions(row + 1)

                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                curr_board[row][col] = "."
        
        find_solutions(0)
        return boards