class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(row, col, prev_val):
            if not 0 <= row < rows or not 0 <= col < cols or matrix[row][col] <= prev_val:
                return 0
            elif (row, col) in dp:
                return dp[(row, col)]
            
            longest_path = 1

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                longest_path = max(longest_path, 1 + dfs(row + dr, col + dc, matrix[row][col]))
            
            dp[(row, col)] = longest_path

            return dp[(row, col)]
        
        longest_path = 0

        for row in range(rows):
            for col in range(cols):
                longest_path = max(longest_path, dfs(row, col, -1))

        return longest_path
    