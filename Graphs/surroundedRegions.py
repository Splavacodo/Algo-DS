class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col):
            if (not 0 <= row < rows or 
                not 0 <= col < cols or
                board[row][col] != "O"):
                return
            
            board[row][col] = "P"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(row + dr, col + dc)
        
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "P":
                    board[row][col] = "O"
        