class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if not 0 <= row < rows or not 0 <= col < cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            return (1 + dfs(row, col - 1) + 
                dfs(row, col + 1) + 
                dfs(row - 1, col) + 
                dfs(row + 1, col))
        
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                max_area = max(dfs(row, col), max_area)
        
        return max_area