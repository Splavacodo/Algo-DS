from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.point_counts = defaultdict(int)
        self.points = []

    def add(self, point: list[int]) -> None:
        self.point_counts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: list[int]) -> int:
        square_count = 0
        px, py = point

        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            
            square_count += self.point_counts[(x, py)] * self.point_counts[(px, y)]
        
        return square_count
