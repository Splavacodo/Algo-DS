from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []

        for x, y in points:
            distance = sqrt(x**2 + y**2)

            distances.append([distance, x, y])
        
        heapq.heapify(distances)
        k_closest = []

        while k > 0:
            point = heapq.heappop(distances)[1:]
            k_closest.append(point)
            k -= 1
        
        return k_closest