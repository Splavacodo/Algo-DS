from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
    
        rotting_oranges = [(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == 2]
        queue = deque(rotting_oranges)

        fresh_oranges = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1

        minutes_passed = 0
        while fresh_oranges > 0 and queue:
            q_len = len(queue)

            for _ in range(q_len):
                row, col = queue.popleft()
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh_oranges -= 1

            minutes_passed += 1
        
        return minutes_passed if fresh_oranges == 0 else -1