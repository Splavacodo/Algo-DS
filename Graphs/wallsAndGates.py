from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: list[list[int]]):
        rows, cols = len(rooms), len(rooms[0])
        INF = 2**31 - 1

        queue = deque([(row, col) for row in range(rows) for col in range(cols) if rooms[row][col] == 0])
        distance = 0

        while queue:
            distance += 1

            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                neighbors = [(col - 1, row), (col + 1, row), (col, row - 1), (col, row + 1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == INF:
                        rooms[r][c] = distance
                        queue.append((r, c))
        
        return rooms