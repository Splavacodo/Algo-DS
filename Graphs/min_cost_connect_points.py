import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        manhattan = lambda point, other_point: abs(point[0] - other_point[0]) + abs(point[1] - other_point[1])

        nodes_to_visit = set([tuple(point) for point in points])
        priority_q = [(0, tuple(points[0]))]
        min_cost = 0

        while nodes_to_visit:
            curr_cost, curr_node = heapq.heappop(priority_q)

            if curr_node not in nodes_to_visit:
                continue
        
            nodes_to_visit.remove(curr_node)
            min_cost += curr_cost

            for node in nodes_to_visit:
                heapq.heappush(priority_q, (manhattan(curr_node, node), node))
        
        return min_cost