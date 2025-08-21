import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        rows = cols = len(grid)
        visited = set((0, 0))
        prio_q = [(grid[0][0], 0, 0)]

        while prio_q:
            max_time, row, col = heapq.heappop(prio_q)

            if row == rows - 1 and col == cols - 1:
                return max_time
            
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row = row + dr
                next_col = col + dc

                if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    heapq.heappush(prio_q, (max(max_time, grid[next_row][next_col]), next_row, next_col))
        