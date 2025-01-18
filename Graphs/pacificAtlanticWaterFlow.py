class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visited, prev_height):
            if (not 0 <= row < rows or 
                not 0 <= col < cols or 
                (row, col) in visited or 
                heights[row][col] < prev_height):
                return
            
            visited.add((row, col))
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
        
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])

        flows_to_both = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    flows_to_both.append((row, col))
        
        return flows_to_both