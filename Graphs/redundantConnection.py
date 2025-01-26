from collections import deque

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        indegrees = [0 for _ in range(len(edges) + 1)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            indegrees[src] += 1
            indegrees[dst] += 1

        queue = deque()

        for i in range(len(edges) + 1):
            if indegrees[i] == 1:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            indegrees[curr] -= 1

            for neighbor in adj[curr]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 1:
                    queue.append(neighbor)
        
        for u, v in edges[::-1]:
            if indegrees[u] == 2 and indegrees[v]:
                return [u, v]
        
        return []