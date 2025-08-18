from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dst, weight in times:
            adj[src].append((dst, weight))
        
        priority_q = [(0, k)]
        visited = set()
        time = 0

        while priority_q:
            curr_time, curr_node = heapq.heappop(priority_q)

            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            time = curr_time

            for dst, weight in adj[curr_node]:
                if dst not in visited:
                    heapq.heappush(priority_q, (curr_time + weight, dst))
        
        return time if len(visited) == n else -1
