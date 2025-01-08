class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if not 0 <= row < rows or not 0 <= col < cols or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            # left
            dfs(row, col - 1)
            # up
            dfs(row - 1, col)
            # right
            dfs(row, col + 1)
            # down
            dfs(row + 1, col)

        num_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1
        
        return num_islands